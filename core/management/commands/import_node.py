"""Eski Node.js versiyasi bazasidan (data/finora.db) kontentni Django'ga ko'chirish.

Ishlatish:  python manage.py import_node --db _node_arxiv/data/finora.db --root _node_arxiv
"""
import json
import sqlite3
from datetime import datetime, timezone as dt_tz
from pathlib import Path

from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from core import models as M

COLLECTIONS = {
    'services': M.Service, 'industries': M.Industry, 'cases': M.Case, 'team': M.TeamMember,
    'clients': M.Client, 'partners': M.Partner, 'stats': M.Stat, 'why': M.WhyCard,
    'steps': M.Step, 'values': M.Value,
}
IMAGE_FIELDS = {'image', 'logo', 'photo', 't_photo'}
SKIP = {'videos', 'gallery', 't_video'}


class Command(BaseCommand):
    help = "Node.js versiyasi bazasidan kontent, sozlamalar, arizalar va fayllarni ko'chiradi"

    def add_arguments(self, parser):
        parser.add_argument('--db', default='data/finora.db', help='Node bazasi (finora.db) yo‘li')
        parser.add_argument('--root', default='.', help='Node loyihasi ildizi (public/ va uploads/ shu yerda)')

    def handle(self, *args, **opts):
        db_path, self.root = Path(opts['db']), Path(opts['root'])
        if not db_path.exists():
            raise CommandError(f'Baza topilmadi: {db_path}')
        con = sqlite3.connect(db_path)
        con.row_factory = sqlite3.Row
        self.missing = []

        with transaction.atomic():
            for model in [*COLLECTIONS.values(), M.Lead]:
                model.objects.all().delete()
            for row in con.execute('SELECT * FROM items ORDER BY col, sort, id'):
                self.import_item(row)
            self.import_settings({r['key']: r['value'] for r in con.execute('SELECT key, value FROM settings')})
            for r in con.execute('SELECT * FROM leads ORDER BY id'):
                lead = M.Lead.objects.create(name=r['name'] or '', phone=r['phone'] or '', service=r['service'] or '',
                                             message=r['message'] or '', source=r['source'] or '',
                                             status=r['status'] or 'new', note=r['note'] or '')
                M.Lead.objects.filter(pk=lead.pk).update(created_at=self.parse_dt(r['created_at']))

        for model in [*COLLECTIONS.values(), M.Lead]:
            self.stdout.write(f'  {model._meta.verbose_name_plural}: {model.objects.count()}')
        for m in self.missing:
            self.stdout.write(self.style.WARNING(f'  Fayl topilmadi: {m}'))
        self.stdout.write(self.style.SUCCESS("Ko'chirish tugadi."))

    # ------------------------------------------------------------------ yordamchilar
    def source_file(self, url):
        url = str(url or '')
        if url.startswith('/uploads/'):
            p = self.root / 'uploads' / Path(url).name
        elif url.startswith('/'):
            p = self.root / 'public' / url.lstrip('/')
        else:
            return None
        if not p.exists():
            self.missing.append(url)
            return None
        return p

    def attach(self, field, url):
        p = self.source_file(url)
        if p:
            with p.open('rb') as f:
                field.save(p.name, File(f), save=False)

    @staticmethod
    def parse_dt(s):
        try:
            return datetime.strptime(s, '%Y-%m-%d %H:%M:%S').replace(tzinfo=dt_tz.utc)
        except (TypeError, ValueError):
            return datetime.now(dt_tz.utc)

    def import_item(self, row):
        model = COLLECTIONS.get(row['col'])
        if not model:
            return
        data = json.loads(row['data'] or '{}')
        names = {f.name for f in model._meta.get_fields()}
        obj = model(sort=row['sort'], active=bool(row['active']))
        for k, v in data.items():
            if k in SKIP or k not in names or k in IMAGE_FIELDS:
                continue
            if isinstance(v, list):
                v = '\n'.join(str(x) for x in v)
            if isinstance(v, bool) or v is None:
                setattr(obj, k, bool(v))
            else:
                setattr(obj, k, str(v))
        for k in IMAGE_FIELDS & names:
            if data.get(k):
                self.attach(getattr(obj, k), data[k])
        obj.save()

        if model in (M.Case, M.TeamMember):
            video_model, image_model, fk = ((M.CaseVideo, M.CaseImage, 'case') if model is M.Case
                                            else (M.MemberVideo, M.MemberImage, 'member'))
            for i, v in enumerate(data.get('videos') or []):
                vid = video_model(**{fk: obj}, sort=i)
                if str(v).startswith('/uploads/'):
                    self.attach(vid.file, v)
                    if not vid.file:
                        continue
                else:
                    vid.url = v
                vid.save()
            for i, u in enumerate(data.get('gallery') or []):
                img = image_model(**{fk: obj}, sort=i)
                self.attach(img.image, u)
                if img.image:
                    img.save()
            if model is M.Case and data.get('t_video'):
                if str(data['t_video']).startswith('/uploads/'):
                    self.attach(obj.t_video_file, data['t_video'])
                else:
                    obj.t_video_url = data['t_video']
                obj.save()

    def import_settings(self, s):
        obj = M.SiteSettings.load()
        names = {f.name for f in M.SiteSettings._meta.get_fields()}
        for k, v in s.items():
            if k in names and k != 'logo' and k != 'id':
                setattr(obj, k, v or '')
        if s.get('logo') and s['logo'] != '/img/logo.png':
            self.attach(obj.logo, s['logo'])
        obj.save()

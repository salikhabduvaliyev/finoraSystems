"""core/ui_translations.py dan locale/{en,ru}/LC_MESSAGES/django.po va .mo fayllarini yaratadi.

    python manage.py build_locale

GNU gettext o'rnatilishi shart emas (Windows'da ham ishlaydi). Shablon va koddagi
tarjima qilinadigan matnlarni tekshirib, lug'atda yo'qlarini ogohlantiradi.
"""
import re
import struct
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from core.ui_translations import UI, URLS

LANGS = {'en': 0, 'ru': 1}
BASE = Path(settings.BASE_DIR)


def found_msgids():
    """Shablonlar va Python fayllaridagi tarjima qilinadigan matnlar."""
    ids = set()
    for f in (BASE / 'core' / 'templates' / 'site').rglob('*.html'):
        t = f.read_text(encoding='utf-8')
        ids.update(m[1] for m in re.findall(r'''\{% translate (["'])(.+?)\1''', t))
        ids.update(re.sub(r'\{\{ (\w+) \}\}', r'%(\1)s', m[1]) for m in
                   re.findall(r'\{% blocktranslate(?: with (\w+)=[\w.]+)? %\}(.+?)\{% endblocktranslate %\}', t, re.S))
        ids.update(m[1] for m in re.findall(r'''_\((["'])(.+?)\1\)''', t))
    for name in ('context.py', 'views.py', 'templatetags/finora.py'):
        t = (BASE / 'core' / name).read_text(encoding='utf-8')
        ids.update(m[1] for m in re.findall(r'''\b_\((["'])(.+?)\1\)''', t))
    return ids


def pct(s):
    """Django shablonlari oddiy % ni %% sifatida qidiradi (%(name)s bundan mustasno)."""
    return re.sub(r'%(?!\()', '%%', s)


def po_escape(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def write_mo(path, catalog):
    """GNU .mo formatida yozish (Python Tools/i18n/msgfmt.py mantig'i)."""
    keys = sorted(catalog)
    ids = strs = b''
    offsets = []
    for k in keys:
        kb, vb = k.encode('utf-8'), catalog[k].encode('utf-8')
        offsets.append((len(ids), len(kb), len(strs), len(vb)))
        ids += kb + b'\0'
        strs += vb + b'\0'
    keystart = 7 * 4 + 16 * len(keys)
    valuestart = keystart + len(ids)
    koffsets, voffsets = [], []
    for o1, l1, o2, l2 in offsets:
        koffsets += [l1, o1 + keystart]
        voffsets += [l2, o2 + valuestart]
    head = struct.pack('<7I', 0x950412de, 0, len(keys), 7 * 4, 7 * 4 + len(keys) * 8, 0, 0)
    table = struct.pack(f'<{len(koffsets) + len(voffsets)}I', *koffsets, *voffsets)
    path.write_bytes(head + table + ids + strs)


class Command(BaseCommand):
    help = "Interfeys tarjimalarini (.po/.mo) ui_translations.py dan yaratadi"

    def handle(self, *args, **opts):
        missing = sorted(found_msgids() - set(UI))
        for m in missing:
            self.stdout.write(self.style.WARNING(f"  Lug'atda yo'q: {m!r}"))

        for lang, idx in LANGS.items():
            plural = 'nplurals=2; plural=(n != 1);' if lang == 'en' else \
                'nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);'
            header = ('Content-Type: text/plain; charset=UTF-8\n'
                      f'Language: {lang}\nPlural-Forms: {plural}\n')
            catalog = {'': header}
            po = ['# Finora Systems — avtomatik yaratilgan: python manage.py build_locale', 'msgid ""', 'msgstr ""']
            po += [f'"{po_escape(line)}\\n"' for line in header.strip().split('\n')]
            for uz, tr in UI.items():
                uz, val = pct(uz), pct(tr[idx])
                catalog[uz] = val
                po += ['', f'msgid "{po_escape(uz)}"', f'msgstr "{po_escape(val)}"']
            for uz, tr in URLS.items():
                catalog[f'url\x04{uz}'] = tr[idx]  # pgettext konteksti
                po += ['', 'msgctxt "url"', f'msgid "{uz}"', f'msgstr "{tr[idx]}"']
            d = BASE / 'locale' / lang / 'LC_MESSAGES'
            d.mkdir(parents=True, exist_ok=True)
            (d / 'django.po').write_text('\n'.join(po) + '\n', encoding='utf-8')
            write_mo(d / 'django.mo', catalog)
            self.stdout.write(f'  {lang}: {len(catalog) - 1} ta tarjima')
        self.stdout.write(self.style.SUCCESS('locale/ yangilandi.'))

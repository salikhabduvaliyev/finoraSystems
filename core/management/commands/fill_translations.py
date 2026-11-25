"""Bo'sh EN/RU maydonlarni core/content_translations.py lug'atidan to'ldirish.

    python manage.py fill_translations          # faqat bo'sh maydonlar
    python manage.py fill_translations --force  # mavjud tarjimalarni ham yangilash

Admin'da qo'lda yozilgan tarjimalar (--force berilmasa) o'zgarmaydi.
"""
from django.core.management.base import BaseCommand
from modeltranslation.translator import translator

from core.content_translations import T

LANGS = {'en': 0, 'ru': 1}


def translate(value, idx):
    """Butun matn lug'atda bo'lsa — shuni; ro'yxat bo'lsa — har bir qatorni alohida."""
    value = str(value or '').replace('\r', '')
    if not value.strip():
        return ''
    if value.strip() in T:
        return T[value.strip()][idx]
    lines = value.split('\n')
    out = [T[l.strip()][idx] if l.strip() in T else l for l in lines]
    return '\n'.join(out) if out != lines else ''


class Command(BaseCommand):
    help = "EN/RU tarjimalarini lug'atdan to'ldiradi"

    def add_arguments(self, parser):
        parser.add_argument('--force', action='store_true', help='mavjud tarjimalar ustidan ham yozish')

    def handle(self, *args, force=False, **kw):
        filled = 0
        for model in translator.get_registered_models():
            fields = translator.get_options_for_model(model).fields
            for obj in model.objects.all():
                changed = []
                for f in fields:
                    src = getattr(obj, f'{f}_uz')
                    for lang, idx in LANGS.items():
                        attr = f'{f}_{lang}'
                        if getattr(obj, attr) and not force:
                            continue
                        tr = translate(src, idx)
                        if tr and tr != getattr(obj, attr):
                            setattr(obj, attr, tr)
                            changed.append(attr)
                if changed:
                    obj.save(update_fields=changed)
                    filled += len(changed)
        self.stdout.write(self.style.SUCCESS(f"To'ldirilgan maydonlar: {filled}"))

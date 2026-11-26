"""Sohasi belgilanmagan keyslarni "Yo'nalish" matni bo'yicha sohaga bog'lash.

    python manage.py link_cases

Faqat aniq mos kelganlarini bog'laydi (soha nomi yoki yorlig'i bir xil bo'lsa).
Admin'da qo'lda tanlangan soha o'zgarmaydi.
"""
from django.core.management.base import BaseCommand

from core.models import Case, Industry


def norm(s):
    return ''.join(ch for ch in str(s or '').lower() if ch.isalnum())


class Command(BaseCommand):
    help = "Keyslarni yo'nalishi bo'yicha sohalarga bog'laydi"

    def handle(self, *args, **opts):
        index = {}
        for ind in Industry.objects.all():
            for value in (ind.title_uz, ind.label_uz, ind.title_en, ind.title_ru):
                if value:
                    index.setdefault(norm(value), ind)
        linked = 0
        for case in Case.objects.filter(industry__isnull=True):
            ind = index.get(norm(case.direction_uz))
            if ind:
                case.industry = ind
                case.save(update_fields=['industry'])
                linked += 1
                self.stdout.write(f'  «{case.title_uz}» → {ind.title_uz}')
        self.stdout.write(self.style.SUCCESS(f"Bog'langan keyslar: {linked}"))

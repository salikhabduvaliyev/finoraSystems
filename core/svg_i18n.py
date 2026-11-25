"""Soha illyustratsiyalari (SVG) ichidagi yozuvlarning EN/RU nusxalarini yaratish.

    python -m core.svg_i18n      # templates/svg/{mock,icon}/{en,ru}/*.svg ni qayta yaratadi

Illyustratsiya o'zgarsa yoki yangi yozuv qo'shilsa — shu lug'atni to'ldirib, qayta ishga tushiring.
"""
from pathlib import Path

# o'zbekcha: (inglizcha, ruscha)
WORDS = {
    '12-oktabr': ('Oct 12', '12 октября'), '14.2 mln': ('14.2M', '14,2 млн'), '48 mln': ('48M', '48 млн'),
    '3 xonali · 86 m²': ('3-room · 86 m²', '3-комн. · 86 м²'), '320 qop': ('320 bags', '320 меш.'),
    '612 dona': ('612 pcs', '612 шт.'), 'APC: 1 482 yo‘lovchi': ('APC: 1,482 passengers', 'APC: 1 482 пассажира'),
    'Aviabilet + mehmonxona': ('Flight + hotel', 'Авиабилет + отель'), 'Bemorlar': ('Patients', 'Пациенты'),
    'Bron': ('Book', 'Бронь'), 'Bugun': ('Today', 'Сегодня'), 'Bugungi qabul': ("Today's appointments", 'Приём на сегодня'),
    'Bugungi savdo': ("Today's sales", 'Продажи сегодня'), 'Buyurtma bajarildi': ('Orders completed', 'Заказы выполнены'),
    'Darslar': ('Lessons', 'Уроки'), 'Dubay · 5 kun': ('Dubai · 5 days', 'Дубай · 5 дней'),
    'Farg‘ona, markaz': ('Fergana, center', 'Фергана, центр'), 'Fuga': ('Grout', 'Затирка'),
    'Funksiyalar': ('Functions', 'Функции'), 'Hovli · 6 sotix': ('House · 6 acres', 'Дом · 6 соток'),
    'Imtihon': ('Exam', 'Экзамен'), 'Ishlab chiqarish buyurtmalari': ('Production orders', 'Производственные заказы'),
    'Jarayonda': ('In progress', 'В работе'), 'Kam!': ('Low!', 'Мало!'), 'Kardiolog': ('Cardiologist', 'Кардиолог'),
    'Keyingi bekat': ('Next stop', 'Следующая'), 'Kirish': ('Intro', 'Введение'), 'Kley M-100': ('Adhesive M-100', 'Клей M-100'),
    'Ko‘rsatuv': ('Viewing', 'Показ'), 'Kutmoqda': ('Waiting', 'Ожидает'), 'Laminat 8 mm': ('Laminate 8 mm', 'Ламинат 8 мм'),
    'Liniyada': ('On route', 'На линии'), 'Loyiha': ('Project', 'Проект'), 'Markaz · 2 daq': ('Center · 2 min', 'Центр · 2 мин'),
    'Navbatda': ('Queued', 'В очереди'), 'Nevrolog': ('Neurologist', 'Невролог'),
    'Oilaviy tur paket': ('Family tour package', 'Семейный турпакет'), 'Ombor qoldig’i': ('Stock levels', 'Остатки на складе'),
    'O‘zgaruvchilar': ('Variables', 'Переменные'), 'Pediatr': ('Pediatrician', 'Педиатр'), 'Plitka 60×60': ('Tile 60×60', 'Плитка 60×60'),
    'Python asoslari · 3-dars': ('Python basics · Lesson 3', 'Основы Python · урок 3'), 'Qabulda': ('In session', 'На приёме'),
    'Qo‘qon': ('Kokand', 'Коканд'), 'Quvvat': ('Power', 'Мощность'), 'Quyosh stansiyasi': ('Solar station', 'Солнечная станция'),
    'Samarqand · 3 kun': ('Samarkand · 3 days', 'Самарканд · 3 дня'), 'Talabalar': ('Students', 'Студенты'),
    'Tayyor ✓': ('Done ✓', 'Готово ✓'), 'Tejam': ('Savings', 'Экономия'), 'Terapevt': ('Therapist', 'Терапевт'),
    'To‘lov': ('Payments', 'Оплата'), 'Tugadi': ('Finished', 'Завершён'), 'Tushum': ('Revenue', 'Выручка'), 'Uy': ('House', 'Дом'),
    'Xonadon': ('Apartment', 'Квартира'), 'Yangi': ('New', 'Новое'), 'Yer': ('Land', 'Участок'), 'Yozilgan': ('Booked', 'Записан'),
    'avtobus': ('buses', 'автобусов'), '● Jonli': ('● Live', '● Онлайн'), '✓ Bron tasdiqlandi': ('✓ Booking confirmed', '✓ Бронь подтверждена'),
    '1 240 m²': ('1,240 m²', '1 240 м²'), 'Foto yuklanadi': ('Photo coming soon', 'Фото скоро'),
}

ROOT = Path(__file__).parent / 'templates' / 'svg'


def build():
    sources = list((ROOT / 'mock').glob('*.svg')) + [ROOT / 'icon' / 'avatar.svg']
    for idx, lang in enumerate(('en', 'ru')):
        for src in sources:
            text = src.read_text(encoding='utf-8')
            for uz, tr in WORDS.items():
                text = text.replace(f'>{uz}</text>', f'>{tr[idx]}</text>')
            out = src.parent / lang / src.name
            out.parent.mkdir(exist_ok=True)
            out.write_text(text, encoding='utf-8')
    print(f'{len(sources)} ta SVG × 2 til yaratildi')


if __name__ == '__main__':
    build()

"""Sayt interfeysi matnlarining tarjimalari (shablonlardagi {% translate %} va koddagi _()).

Kalit — o'zbekcha matn, qiymat — (inglizcha, ruscha).
O'zgartirgandan keyin:  python manage.py build_locale   (locale/*.po va *.mo ni yangilaydi)
"""

UI = {
    # ---- Umumiy / menyu / footer
    'ERP, CRM va biznes avtomatlashtirish': ('ERP, CRM and business automation', 'ERP, CRM и автоматизация бизнеса'),
    'Bosh sahifa': ('Home', 'Главная'),
    'Asosiy menyu': ('Main menu', 'Главное меню'),
    'Til': ('Language', 'Язык'),
    'Konsultatsiya': ('Consultation', 'Консультация'),
    'Menyu': ('Menu', 'Меню'),
    'Sahifalar': ('Pages', 'Страницы'),
    'Xizmatlar': ('Services', 'Услуги'),
    'Sohalar': ('Industries', 'Отрасли'),
    'Keyslar': ('Case studies', 'Кейсы'),
    'Jamoa': ('Team', 'Команда'),
    'Aloqa': ('Contact', 'Контакты'),
    'Bepul audit olish': ('Get a free audit', 'Получить бесплатный аудит'),
    'Barcha huquqlar himoyalangan.': ('All rights reserved.', 'Все права защищены.'),
    'Tepaga': ('Back to top', 'Наверх'),
    'Sahifa topilmadi': ('Page not found', 'Страница не найдена'),
    "Havola eskirgan yoki noto'g'ri yozilgan bo'lishi mumkin.": (
        'The link may be outdated or mistyped.', 'Ссылка устарела или указана с ошибкой.'),
    'Bosh sahifaga qaytish': ('Back to home', 'Вернуться на главную'),

    # ---- Bosh sahifa
    'Bepul audit': ('Free audit', 'Бесплатный аудит'),
    'Rasmiy hamkor': ('Official partner', 'Официальный партнёр'),
    'Nega Finora': ('Why Finora', 'Почему Finora'),
    'Oldingi': ('Previous', 'Назад'),
    'Keyingi': ('Next', 'Вперёд'),
    "Yo'nalish": ('Industry', 'Направление'),
    'Barcha keyslar': ('All case studies', 'Все кейсы'),
    'Ishonch': ('Trust', 'Доверие'),
    'Jarayon': ('Process', 'Процесс'),
    "To'liq jamoa bilan tanishish": ('Meet the whole team', 'Познакомиться со всей командой'),
    'Jonli · bugungi savdo': ("Live · today's sales", 'Онлайн · продажи сегодня'),
    'Savdo': ('Sales', 'Продажи'),
    'mln': ('M', 'млн'),
    'Buyurtmalar': ('Orders', 'Заказы'),
    'Foyda': ('Profit', 'Прибыль'),
    'Buyurtma tayyor': ('Order ready', 'Заказ готов'),
    "+38% o'sish": ('+38% growth', 'Рост +38%'),
    'AI bot javob berdi': ('AI bot replied', 'AI-бот ответил'),

    # ---- Xizmatlar / sohalar / keyslar sahifalari
    "To'liq IT yechimlar": ('End-to-end IT solutions', 'Комплексные IT-решения'),
    "Tahlildan ishga tushirish va o'qitishgacha.": (
        'From analysis to launch and training.', 'От анализа до запуска и обучения.'),
    "Sohangiz og'rig'iga mos yechim": ("Solutions for your industry's pain points", 'Решения для болевых точек вашей отрасли'),
    'Har bir soha uchun: muammo → tizim → AI va veb-sayt.': (
        'For every industry: problem → system → AI and website.', 'Для каждой отрасли: проблема → система → AI и сайт.'),
    "Og'riq nuqtalari": ('Pain points', 'Болевые точки'),
    'Bizning yechim': ('Our solution', 'Наше решение'),
    'AI yechim': ('AI solution', 'AI-решение'),
    'Veb-sayt': ('Website', 'Сайт'),
    'Konsultatsiya olish': ('Get a consultation', 'Получить консультацию'),
    'Amalga oshirilgan loyihalar': ('Completed projects', 'Реализованные проекты'),
    'Biz tizimlashtirgan bizneslar va ularning natijalari.': (
        'Businesses we have systematized and their results.', 'Бизнесы, которые мы систематизировали, и их результаты.'),
    'Natija': ('Result', 'Результат'),
    'Batafsil ko‘rish': ('View details', 'Подробнее'),

    # ---- Keys ichki sahifasi
    'Yo‘l': ('Breadcrumb', 'Навигация'),
    'Keys': ('Case study', 'Кейс'),
    'Mijoz': ('Client', 'Клиент'),
    'Muddat': ('Duration', 'Срок'),
    'Yil': ('Year', 'Год'),
    'Shunday tizim kerak': ('I need a system like this', 'Хочу такую систему'),
    'Natijalar': ('Results', 'Результаты'),
    'Raqamlarda natija': ('Results in numbers', 'Результаты в цифрах'),
    'Vazifa': ('Challenge', 'Задача'),
    'Mijoz nimaga duch kelgan': ('What the client was facing', 'С чем столкнулся клиент'),
    'Yechim': ('Solution', 'Решение'),
    'Biz nima qildik': ('What we did', 'Что мы сделали'),
    'Bajarilgan ishlar': ('Work done', 'Выполненные работы'),
    'Loyiha doirasida': ('Within the project', 'В рамках проекта'),
    'Loyihadan videolar': ('Project videos', 'Видео проекта'),
    'Video': ('Video', 'Видео'),
    'Galereya': ('Gallery', 'Галерея'),
    'Loyihadan lavhalar': ('Project highlights', 'Кадры проекта'),
    'Video-otziv': ('Video testimonial', 'Видеоотзыв'),
    'Mijoz fikri': ('Testimonial', 'Отзыв клиента'),
    'Mijozimiz nima deydi': ('What our client says', 'Что говорит наш клиент'),
    'Boshqa loyihalar': ('Other projects', 'Другие проекты'),
    'Videoni ko‘rish': ('Watch video', 'Смотреть видео'),

    'Oldingi keys': ('Previous case', 'Предыдущий кейс'),
    'Keyingi keys': ('Next case', 'Следующий кейс'),
    'Keyingi keyslar': ('More case studies', 'Следующие кейсы'),
    'Soha': ('Industry', 'Отрасль'),

    # ---- Soha ichki sahifasi
    'Soha haqida': ('About the industry', 'Об отрасли'),
    'Muammo va yechim': ('Problem and solution', 'Проблема и решение'),
    'Qanday muammolarni hal qilamiz': ('What problems we solve', 'Какие проблемы мы решаем'),
    'Qo‘shimcha imkoniyatlar': ('Additional capabilities', 'Дополнительные возможности'),
    'AI va veb-sayt': ('AI and website', 'AI и сайт'),
    'Taqdimotlar': ('Presentations', 'Презентации'),
    'Yechim taqdimoti': ('Solution presentation', 'Презентация решения'),
    'Taqdimotni ko‘rish': ('View presentation', 'Смотреть презентацию'),
    'Yangi oynada ochish': ('Open in new tab', 'Открыть в новом окне'),
    'Yuklab olish': ('Download', 'Скачать'),
    'Ochish': ('Open', 'Открыть'),
    'Sohaga oid videolar': ('Industry videos', 'Видео по отрасли'),
    'Shu sohadagi loyihalarimiz': ('Our projects in this industry', 'Наши проекты в этой отрасли'),
    'Boshqa sohalar': ('Other industries', 'Другие отрасли'),
    'Barcha sohalar': ('All industries', 'Все отрасли'),

    # ---- Xizmatlar: materiallar
    'Materiallar': ('Resources', 'Материалы'),
    'Taqdimotlar va videolar': ('Presentations and videos', 'Презентации и видео'),
    'Xizmatlarimiz bo‘yicha taqdimotlar va video sharhlar — qulay vaqtda tanishib chiqing.': (
        'Presentations and video overviews of our services — explore them at your convenience.',
        'Презентации и видеообзоры наших услуг — изучайте в удобное время.'),
    'Xizmat bo‘yicha saralash': ('Filter by service', 'Фильтр по услуге'),
    'Hammasi': ('All', 'Все'),
    'Taqdimot': ('Presentation', 'Презентация'),
    'Videolar': ('Videos', 'Видео'),
    'Ko‘rish': ('View', 'Смотреть'),

    # ---- Jamoa
    'Bizning jamoa': ('Our team', 'Наша команда'),
    "Jamoa bilan bog'lanish": ('Contact the team', 'Связаться с командой'),
    'Asoschi': ('Founder', 'Основатель'),
    "Ta'lim": ('Education', 'Образование'),
    'Tajriba': ('Experience', 'Опыт'),
    'Ekspertiza': ('Expertise', 'Экспертиза'),
    'Qadriyatlar': ('Values', 'Ценности'),
    'Biz nimaga ishonamiz': ('What we believe in', 'Во что мы верим'),
    'Bog‘lanish': ('Contact', 'Связаться'),
    'Haqida': ('About', 'О себе'),
    'Ko‘nikmalar': ('Skills', 'Навыки'),
    'Sertifikat va yutuqlar': ('Certificates and achievements', 'Сертификаты и достижения'),
    'Rasmlar': ('Photos', 'Фотографии'),
    'Jamoaning boshqa a’zolari': ('Other team members', 'Другие участники команды'),
    '%(name)s — videolar': ('%(name)s — videos', '%(name)s — видео'),
    '%(name)s haqida batafsil ma’lumot tez orada qo‘shiladi.': (
        'More about %(name)s coming soon.', 'Подробная информация о %(name)s скоро появится.'),

    # ---- Ariza bloki / forma
    'Bepul konsultatsiya': ('Free consultation', 'Бесплатная консультация'),
    "Ma'lumot qoldiring, 1 ish kuni ichida bog'lanamiz.": (
        'Leave your details and we will contact you within 1 business day.', 'Оставьте заявку — свяжемся в течение 1 рабочего дня.'),
    'Qanday ishlaymiz': ('How we work', 'Как мы работаем'),
    '<b>1 ish kuni</b> ichida bog‘lanamiz': ('We reply within <b>1 business day</b>', 'Свяжемся в течение <b>1 рабочего дня</b>'),
    '<b>Bepul audit</b> va mutaxassis tavsiyalari': ('<b>Free audit</b> and expert advice', '<b>Бесплатный аудит</b> и рекомендации эксперта'),
    "Ma'lumotlaringiz to‘liq <b>maxfiy</b> saqlanadi": ('Your data stays fully <b>confidential</b>', 'Ваши данные полностью <b>конфиденциальны</b>'),
    'Ismingiz': ('Your name', 'Ваше имя'),
    'Telefon raqamingiz': ('Your phone number', 'Ваш номер телефона'),
    'Telefon: +998 __ ___ __ __': ('Phone: +998 __ ___ __ __', 'Телефон: +998 __ ___ __ __'),
    'Qiziqqan xizmat': ('Service you need', 'Интересующая услуга'),
    'Boshqa': ('Other', 'Другое'),
    'Qisqacha vazifa': ('Briefly describe your task', 'Кратко опишите задачу'),
    'Ariza yuborish': ('Send request', 'Отправить заявку'),

    # ---- JavaScript va server xabarlari
    'Yuborilmoqda…': ('Sending…', 'Отправляем…'),
    'Ismingizni yozing — kimga qo‘ng‘iroq qilishni bilishimiz uchun.': (
        'Please enter your name so we know who to call.', 'Укажите имя — чтобы мы знали, кому звонить.'),
    'Telefon raqamini to‘liq yozing, masalan: 90 123-45-67.': (
        'Please enter your full phone number, e.g. 90 123-45-67.', 'Укажите номер телефона полностью, например: 90 123-45-67.'),
    'Ariza yuborilmadi — internet aloqasini tekshirib, qayta urinib ko‘ring.': (
        "The request wasn't sent — check your internet connection and try again.",
        'Заявка не отправлена — проверьте подключение к интернету и попробуйте ещё раз.'),
    'Rahmat! Arizangiz qabul qilindi.': ('Thank you! Your request has been received.', 'Спасибо! Ваша заявка принята.'),
    '1 ish kuni ichida siz bilan bog‘lanamiz.': ('We will contact you within 1 business day.', 'Мы свяжемся с вами в течение 1 рабочего дня.'),
    'Yopish': ('Close', 'Закрыть'),
    "So'rov noto'g'ri.": ('Invalid request.', 'Некорректный запрос.'),
    "Juda ko'p ariza yuborildi. Birozdan keyin qayta urinib ko'ring yoki bizga qo'ng'iroq qiling.": (
        'Too many requests. Please try again later or give us a call.',
        'Слишком много заявок. Попробуйте позже или позвоните нам.'),
    'Ismingizni yozing.': ('Please enter your name.', 'Укажите ваше имя.'),
    "Telefon raqamini to'liq yozing, masalan: 90 123-45-67.": (
        'Please enter your full phone number, e.g. 90 123-45-67.', 'Укажите номер телефона полностью, например: 90 123-45-67.'),
}

# URL bo'laklari (pgettext 'url' konteksti): /xizmatlar -> /en/services -> /ru/uslugi
URLS = {
    'xizmatlar': ('services', 'uslugi'),
    'sohalar': ('industries', 'otrasli'),
    'keyslar': ('cases', 'keysy'),
    'jamoa': ('team', 'komanda'),
    'aloqa': ('contact', 'kontakty'),
}

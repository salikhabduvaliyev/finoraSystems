"""Mavjud kontentning ingliz va rus tarjimalari.

Kalit — o'zbekcha matn (yoki ro'yxatdagi bitta qator), qiymat — (inglizcha, ruscha).
`python manage.py fill_translations` buyrug'i bo'sh EN/RU maydonlarini shu lug'atdan to'ldiradi.
Admin'da qo'lda yozilgan tarjimalar ustidan yozilmaydi.
"""

T = {
    # ---- Xizmatlar
    'Odoo va МойСклад': ('Odoo and MoySklad', 'Odoo и МойСклад'),
    'Ombor va savdo': ('Warehouse and sales', 'Склад и продажи'),
    'Ishlab chiqarish': ('Manufacturing', 'Производство'),
    'Maosh va hisobotlar': ('Payroll and reports', 'Зарплата и отчёты'),
    'ERP joriy etish': ('ERP implementation', 'Внедрение ERP'),
    'Savdo voronkalari': ('Sales funnels', 'Воронки продаж'),
    'Skript va KPI': ('Scripts and KPIs', 'Скрипты и KPI'),
    "Sotuvchilarni o'qitish": ('Sales team training', 'Обучение менеджеров по продажам'),
    "CRM va savdo bo'limi": ('CRM and sales department', 'CRM и отдел продаж'),
    'Tizimlashtirish': ('Systematization', 'Систематизация'),
    'Jarayon xaritasi': ('Process map', 'Карта процессов'),
    'Reglament': ('Regulations', 'Регламенты'),
    'Avtomatlashtirish': ('Automation', 'Автоматизация'),
    'Biznes jarayonlar': ('Business processes', 'Бизнес-процессы'),
    'Davomat va nazorat': ('Attendance and access control', 'Учёт посещаемости и контроль'),
    'Xodimlar davomati': ('Employee attendance', 'Учёт посещаемости сотрудников'),
    'Kirish nazorati': ('Access control', 'Контроль доступа'),
    'ERP integratsiya': ('ERP integration', 'Интеграция с ERP'),
    'Sayt va Telegram': ('Website and Telegram', 'Сайт и Telegram'),
    'Savdo boti': ('Sales bot', 'Бот продаж'),
    "Qo'llab-quvvatlash": ('Customer support', 'Поддержка клиентов'),
    'CRM bilan ulash': ('CRM integration', 'Интеграция с CRM'),
    'AI botlar': ('AI bots', 'AI-боты'),
    'Mobil ilova, platforma': ('Mobile apps, platforms', 'Мобильные приложения, платформы'),
    "To'lov va POS API": ('Payment and POS API', 'Платёжные и POS API'),
    'Mobil ilova (iOS/Android)': ('Mobile app (iOS/Android)', 'Мобильное приложение (iOS/Android)'),
    'LMS va portal': ('LMS and portals', 'LMS и порталы'),
    'Maxsus dasturlar': ('Custom software', 'Индивидуальная разработка'),

    # ---- Sohalar
    'Savdo boti katalog, narx va buyurtmani 24/7 qabul qiladi': (
        'A sales bot handles catalog, prices and orders 24/7',
        'Бот продаж 24/7 показывает каталог, цены и принимает заказы'),
    'Savdo': ('Retail', 'Торговля'),
    "Qoldiq va ombor hisobi o'zaro mos kelmaydi": (
        "Stock levels and warehouse records don't match", 'Остатки и складской учёт не сходятся'),
    "Buyurtmalar Telegram va qo'ng'iroqlarda yo'qolib ketadi": (
        'Orders get lost in Telegram chats and phone calls', 'Заказы теряются в Telegram и звонках'),
    'Onlayn katalog va buyurtma sayti (plitka vizualizatsiyasi bilan)': (
        'Online catalog and ordering website (with tile visualization)',
        'Онлайн-каталог и сайт заказов (с визуализацией плитки)'),
    'Plitka, qurilish materiallari, ulgurji va chakana savdo.': (
        'Tiles, building materials, wholesale and retail.', 'Плитка, стройматериалы, опт и розница.'),
    'Savdo va ombor': ('Retail and warehouse', 'Торговля и склад'),
    'Odoo / МойСклад: yagona ombor va savdo hisobi': (
        'Odoo / MoySklad: unified warehouse and sales accounting', 'Odoo / МойСклад: единый учёт склада и продаж'),
    'amoCRM voronka: har bir mijoz nazoratda': (
        'amoCRM funnel: every customer under control', 'Воронка amoCRM: каждый клиент под контролем'),
    'Avtomatik buyurtma, nasiya va qarzdorlik hisobi': (
        'Automated orders, installments and receivables', 'Автоматические заказы, рассрочка и учёт задолженности'),
    "Ovozli so'rov bilan kunlik ishlab chiqarish hisoboti beruvchi AI agent": (
        'An AI agent that gives daily production reports on voice request',
        'AI-агент, который по голосовому запросу выдаёт ежедневный отчёт по производству'),
    "Hom ashyo sarfi va tannarx noma'lum": (
        'Raw material usage and cost price are unknown', 'Расход сырья и себестоимость неизвестны'),
    "Sexlar o'rtasidagi ichki o'tkazma qog'ozda yuradi": (
        'Internal transfers between workshops are done on paper', 'Внутренние перемещения между цехами ведутся на бумаге'),
    'Zavod korporativ sayti va B2B buyurtma portali': (
        'Corporate factory website and B2B ordering portal', 'Корпоративный сайт завода и B2B-портал заказов'),
    "Zavod va sexlar: hom ashyo, retsept, ichki o'tkazma, tannarx.": (
        'Factories and workshops: raw materials, recipes, internal transfers, cost price.',
        'Заводы и цеха: сырьё, рецептуры, внутренние перемещения, себестоимость.'),
    'Ishlab chiqarish buyurtmalari va retseptlar (BoM)': (
        'Production orders and recipes (BoM)', 'Производственные заказы и рецептуры (BoM)'),
    'Ichki talabnoma sahifasi: ombor → sex': (
        'Internal requisition page: warehouse → workshop', 'Страница внутренних заявок: склад → цех'),
    'Tannarx va chiqindi hisobi real vaqtda': (
        'Real-time cost price and waste tracking', 'Учёт себестоимости и отходов в реальном времени'),
    'AI yordamchi talabaga savol-javob va kurs tavsiyasini beradi': (
        'An AI assistant answers student questions and recommends courses',
        'AI-помощник отвечает на вопросы студентов и рекомендует курсы'),
    "Ta'lim": ('Education', 'Образование'),
    "To'lov va davomat qo'lda yuritiladi": (
        'Payments and attendance are tracked manually', 'Оплаты и посещаемость ведутся вручную'),
    'Kurs sotuvi Instagram va Telegramda tarqoq': (
        'Course sales are scattered across Instagram and Telegram', 'Продажи курсов разбросаны по Instagram и Telegram'),
    'Kurs sotuvchi sayt va talaba shaxsiy kabineti': (
        'Course sales website and student portal', 'Сайт продажи курсов и личный кабинет студента'),
    "Universitetlar, o'quv markazlari va kurs sotuvchi kompaniyalar.": (
        'Universities, training centers and online course companies.',
        'Университеты, учебные центры и компании, продающие курсы.'),
    'LMS: kurs yuklash, sotish va sertifikat': (
        'LMS: course upload, sales and certificates', 'LMS: загрузка и продажа курсов, сертификаты'),
    "CRM voronka va qabul bo'limi": ('CRM funnel and admissions office', 'CRM-воронка и приёмная комиссия'),
    "Click/Payme to'lov va davomat nazorati": (
        'Click/Payme payments and attendance tracking', 'Оплата через Click/Payme и контроль посещаемости'),
    'AI qabul boti: yozilish, eslatma va savollarga javob': (
        'AI reception bot: bookings, reminders and answers to questions',
        'AI-бот регистратуры: запись, напоминания и ответы на вопросы'),
    'Klinika': ('Clinics', 'Клиники'),
    'Transport': ('Transport', 'Транспорт'),
    "Navbat qog'ozda, bemor uzoq kutadi": (
        'Queues are on paper, patients wait for a long time', 'Очередь на бумаге, пациенты долго ждут'),
    "Shifokor yuklamasi va tushum ko'rinmaydi": (
        "Doctors' workload and revenue are not visible", 'Не видно загрузку врачей и выручку'),
    'Klinika sayti: shifokorlar, narxlar, onlayn yozilish': (
        'Clinic website: doctors, prices, online booking', 'Сайт клиники: врачи, цены, онлайн-запись'),
    'Xususiy klinikalar va shifoxonalar.': ('Private clinics and hospitals.', 'Частные клиники и больницы.'),
    'Onlayn navbat va shifokor jadvali': ('Online queue and doctor schedules', 'Онлайн-очередь и расписание врачей'),
    'Bemor kartasi va xizmatlar hisobi': ('Patient records and service accounting', 'Карта пациента и учёт услуг'),
    'Kassa va shifokor ulushi hisobi': (
        "Cash desk and doctors' share accounting", 'Касса и учёт доли врачей'),
    "AI maslahatchi yo'nalish tanlaydi va narxni hisoblaydi": (
        'An AI consultant picks a destination and calculates the price',
        'AI-консультант подбирает направление и рассчитывает стоимость'),
    'Turizm': ('Tourism', 'Туризм'),
    'Bronlar Excel va xabarlarda adashadi': (
        'Bookings get mixed up in Excel and messages', 'Брони путаются в Excel и переписках'),
    'Hamkorlar bilan hisob-kitob chalkash': (
        'Settlements with partners are confusing', 'Расчёты с партнёрами запутаны'),
    "Tur paketlar sayti, onlayn bron va to'lov": (
        'Tour packages website, online booking and payment', 'Сайт турпакетов, онлайн-бронирование и оплата'),
    'Tur operatorlar va sayohat agentliklari.': ('Tour operators and travel agencies.', 'Туроператоры и турагентства.'),
    'Bronlash va paketlar boshqaruvi': ('Booking and package management', 'Управление бронированиями и пакетами'),
    'Mijozlar bazasi va CRM': ('Customer database and CRM', 'Клиентская база и CRM'),
    'Agent va hamkor hisob-kitobi': ('Agent and partner settlements', 'Расчёты с агентами и партнёрами'),
    'AI tahlil xavfli holat va haydovchi xatti-harakatini aniqlaydi': (
        'AI analytics detects dangerous situations and driver behavior',
        'AI-аналитика выявляет опасные ситуации и поведение водителя'),
    "Avtobus joyi va yo'lovchi soni noma'lum": (
        'Bus locations and passenger counts are unknown', 'Местоположение автобусов и число пассажиров неизвестны'),
    'Haydovchi nazorati va hodisalar dalilsiz': (
        'No driver monitoring and no evidence of incidents', 'Нет контроля водителей и доказательств инцидентов'),
    "Monitoring dashboard va yo'lovchi axborot sayti": (
        'Monitoring dashboard and passenger information website', 'Панель мониторинга и информационный сайт для пассажиров'),
    "Avtobus parklari va yo'lovchi tashish tizimlari.": (
        'Bus fleets and passenger transport systems.', 'Автобусные парки и системы пассажирских перевозок.'),
    'MDVR: video va GPS nazorat': ('MDVR: video and GPS monitoring', 'MDVR: видео- и GPS-контроль'),
    "APC: yo'lovchi sanash va hisobot": ('APC: passenger counting and reports', 'APC: подсчёт пассажиров и отчёты'),
    'LED tablo va marshrut axboroti': ('LED displays and route information', 'LED-табло и информация о маршруте'),

    # ---- Keyslar
    "Bir nechta filial va omborlar bitta ERPga jamlandi: savdo, ombor va hisobotlar bir joyda ko'rinadi.": (
        'Multiple branches and warehouses were unified into one ERP: sales, stock and reports in one place.',
        'Несколько филиалов и складов объединены в одной ERP: продажи, склад и отчёты в одном месте.'),
    '___% tezroq hisobot': ('___% faster reporting', 'Отчёты на ___% быстрее'),
    "Plitka tarmog'i uchun yagona Odoo tizimi": (
        'A unified Odoo system for a tile retail chain', 'Единая система Odoo для сети магазинов плитки'),
    "amoCRM jarayonlari qayta ko'rib chiqildi, sotuvchilar uchun skript va o'qitish tayyorlandi.": (
        'amoCRM processes were redesigned; sales scripts and training were prepared.',
        'Процессы в amoCRM пересмотрены, для менеджеров подготовлены скрипты и обучение.'),
    'Savdo va ishlab chiqarish': ('Sales and manufacturing', 'Торговля и производство'),
    "Savdo bo'limi tizimga solindi": ('The sales department was systematized', 'Отдел продаж приведён в систему'),
    "Avtobuslarda video nazorat, yo'lovchi sanash va LED tablo tizimi yagona monitoringga ulandi.": (
        'Video surveillance, passenger counting and LED displays on buses were connected to a single monitoring system.',
        'Видеонаблюдение, подсчёт пассажиров и LED-табло в автобусах подключены к единому мониторингу.'),
    '___ ta avtobus': ('___ buses', '___ автобусов'),
    'Avtobus parki': ('Bus fleet', 'Автобусный парк'),
    'Jamoat transporti uchun MDVR va APC yechimi': (
        'MDVR and APC solution for public transport', 'Решение MDVR и APC для общественного транспорта'),
    'Savdo jarayoni sozlandi, hujjatlar uchun maxsus chop etish shablonlari yaratildi.': (
        'The sales process was configured and custom document print templates were created.',
        'Настроен процесс продаж, созданы индивидуальные шаблоны печати документов.'),
    'Plitka savdosi': ('Tile retailer', 'Магазин плитки'),
    "Plitka savdosi МойСклад'da avtomatlashtirildi": (
        'Tile sales automated in MoySklad', 'Продажи плитки автоматизированы в МойСклад'),
    'Oylik moduli': ('Payroll module', 'Модуль зарплаты'),
    "30 xodim uchun avans, bonus va reja bo'yicha hisob.": (
        'Advances, bonuses and plan-based pay calculation for 30 employees.',
        'Расчёт авансов, бонусов и оплаты по плану для 30 сотрудников.'),
    '___ soat tejaldi': ('___ hours saved', 'Сэкономлено ___ часов'),
    'Ishlab chiqarish korxonasi': ('Manufacturing company', 'Производственное предприятие'),
    'Maosh avtomatlashtirish': ('Payroll automation', 'Автоматизация расчёта зарплаты'),
    'Professorlar kurs yuklaydi, talabalar sotib oladi.': (
        'Professors upload courses, students purchase them.', 'Преподаватели загружают курсы, студенты их покупают.'),
    '___ ta kurs': ('___ courses', '___ курсов'),
    "Korea–O'zbekiston LMS": ('Korea–Uzbekistan LMS', 'LMS Корея–Узбекистан'),
    'Qabul, mijozlar bazasi va kassa hisobi.': (
        'Reception, patient database and cash accounting.', 'Регистратура, база пациентов и учёт кассы.'),
    '___ ta bemor': ('___ patients', '___ пациентов'),
    'Klinika ERP': ('Clinic ERP', 'ERP для клиники'),
    'Loyiha boshqaruvi': ('Project management', 'Управление проектами'),
    'Quyosh paneli loyihalari, montaj bosqichlari va ombor hisobi yagona tizimda.': (
        'Solar panel projects, installation stages and inventory in a single system.',
        'Проекты солнечных панелей, этапы монтажа и складской учёт в единой системе.'),
    '___ ta obyekt': ('___ sites', '___ объектов'),
    'Energetika': ('Energy', 'Энергетика'),
    'Loyiha va montaj nazorati': ('Project and installation control', 'Контроль проектов и монтажа'),

    # ---- Jamoa
    'Propix Group: asoschi va Project Manager': ('Propix Group: founder and Project Manager', 'Propix Group: основатель и Project Manager'),
    'Hamroh Nasiya Savdo: ichki boshqaruv tizimi (ERP)': (
        'Hamroh Nasiya Savdo: internal management system (ERP)', 'Hamroh Nasiya Savdo: внутренняя система управления (ERP)'),
    '5+ yil jamoa boshqaruvi': ('5+ years of team management', '5+ лет управления командой'),
    'CRM / ERP joriy etish': ('CRM / ERP implementation', 'Внедрение CRM / ERP'),
    'Biznes jarayonlar va KPI': ('Business processes and KPIs', 'Бизнес-процессы и KPI'),
    'МойСклад rasmiy hamkori': ('Official MoySklad partner', 'Официальный партнёр МойСклад'),
    'Asoschi · Project Manager': ('Founder · Project Manager', 'Основатель · Project Manager'),
    'TATU: Dasturiy injiniring (2018–2022)': ('TUIT: Software Engineering (2018–2022)', 'ТУИТ: Программная инженерия (2018–2022)'),
    "2020 yildan beri biznes jarayonlarini tizimlashtirish, CRM/ERP avtomatlashtirish va loyiha boshqaruvi bo'yicha ishlaydi. Mahalliy va xalqaro kompaniyalar bilan hamkorlik qilgan.": (
        'Since 2020 he has worked on business process systematization, CRM/ERP automation and project management, partnering with local and international companies.',
        'С 2020 года занимается систематизацией бизнес-процессов, автоматизацией CRM/ERP и управлением проектами. Сотрудничал с местными и международными компаниями.'),
    'Marketing - CRM mutaxassisi': ('Marketing & CRM specialist', 'Специалист по маркетингу и CRM'),
    'AI va avtomatlashtirish muhandisi': ('AI and automation engineer', 'Инженер по AI и автоматизации'),
    'Brand face - Mobilograf': ('Brand face · Mobile videographer', 'Лицо бренда · мобилограф'),
    'Odoo / ERP konsultant': ('Odoo / ERP consultant', 'Консультант Odoo / ERP'),
    'CRM mutaxassisi': ('CRM specialist', 'Специалист по CRM'),

    # ---- Raqamlar
    'bajarilgan loyiha': ('completed projects', 'завершённых проектов'),
    'amaliy tajriba': ('of hands-on experience', 'практического опыта'),
    '7+ yil': ('7+ years', '7+ лет'),
    '6 yil': ('6 years', '6 лет'),
    "soha bo'yicha tayyor yechim": ('industries with ready-made solutions', 'отраслей с готовыми решениями'),
    'birinchi natijagacha': ('to the first results', 'до первого результата'),
    '30 kun': ('30 days', '30 дней'),

    # ---- Nega Finora
    "Avval jarayon, raqam va mas'uliyatni o'rganamiz, shundan keyingina dastur tanlaymiz yoki yozamiz.": (
        'We study your processes, numbers and responsibilities first — only then do we choose or build software.',
        'Сначала изучаем процессы, цифры и зоны ответственности — и только потом выбираем или пишем программу.'),
    'Biznesni tushunamiz': ('We understand business', 'Понимаем бизнес'),
    "Ishlamayotgan narsani topshirmaymiz: har bosqich sinovdan o'tadi va siz bilan kelishiladi.": (
        "We never hand over something that doesn't work: every stage is tested and agreed with you.",
        'Не сдаём то, что не работает: каждый этап проходит проверку и согласовывается с вами.'),
    'Har bosqich tekshiriladi': ('Every stage is tested', 'Каждый этап проверяется'),
    "МойСклад, amoCRM va Odoo bo'yicha rasmiy hamkormiz: litsenziya, sozlash va qo'llab-quvvatlash bir joyda.": (
        "We're an official MoySklad, amoCRM and Odoo partner: licenses, setup and support in one place.",
        'Мы официальный партнёр МойСклад, amoCRM и Odoo: лицензии, настройка и поддержка в одном месте.'),
    'Rasmiy hamkorlik': ('Official partnerships', 'Официальное партнёрство'),

    # ---- Ish jarayoni
    "Biznesingiz qanday ishlashini, bugungi raqamlar va og'riq nuqtalarini birga ko'rib chiqamiz.": (
        'Together we review how your business works, its current numbers and pain points.',
        'Вместе разбираем, как работает ваш бизнес, текущие показатели и болевые точки.'),
    'Tanishuv va audit': ('Introduction and audit', 'Знакомство и аудит'),
    "Jarayon, hisobot va hujjatlarni tahlil qilib, vaqt va pul qayerda yo'qolayotganini aniqlaymiz.": (
        'We analyze processes, reports and documents to find where time and money are being lost.',
        'Анализируем процессы, отчёты и документы и находим, где теряются время и деньги.'),
    'Diagnostika': ('Diagnostics', 'Диагностика'),
    "Kim nima qiladi, ko'rsatkich qanday hisoblanadi, muddat va narx: hammasi hujjatga tushadi.": (
        'Who does what, how metrics are calculated, timeline and price — everything is documented.',
        'Кто что делает, как считаются показатели, сроки и цена — всё фиксируется в документе.'),
    'Texnik topshiriq': ('Technical specification', 'Техническое задание'),
    "Tizim tuzilmasini chizamiz va asosiy ekranlarni ko'rsatamiz. Tasdiqlamay qurmaymiz.": (
        "We design the system architecture and show the key screens. Nothing is built until you approve it.",
        'Проектируем структуру системы и показываем ключевые экраны. Без согласования не строим.'),
    'Arxitektura va prototip': ('Architecture and prototype', 'Архитектура и прототип'),
    'Odoo, МойСклад, amoCRM sozlanadi, kerak joyda maxsus modul va integratsiya yoziladi.': (
        'Odoo, MoySklad and amoCRM are configured; custom modules and integrations are built where needed.',
        'Настраиваем Odoo, МойСклад, amoCRM, при необходимости пишем модули и интеграции.'),
    'Sozlash va ishlab chiqish': ('Configuration and development', 'Настройка и разработка'),
    "Eski tizim va Excel'dagi ma'lumotlar ko'chiriladi, to'g'riligi qayta tekshiriladi.": (
        'Data from legacy systems and Excel is migrated and double-checked for accuracy.',
        'Переносим данные из старой системы и Excel и повторно проверяем их корректность.'),
    "Ma'lumotlarni ko'chirish": ('Data migration', 'Перенос данных'),
    "Xodimlar lavozimiga qarab o'qitiladi, har biriga qisqa yo'riqnoma topshiriladi.": (
        'Employees are trained according to their roles, and each receives a short guide.',
        'Обучаем сотрудников по ролям и выдаём каждому краткую инструкцию.'),
    "O'qitish va ishga tushirish": ('Training and launch', 'Обучение и запуск'),
    "Dastlabki oylarda yonida bo'lamiz, xatolarni tuzatamiz va yangi imkoniyatlar qo'shamiz.": (
        'We stay with you in the first months, fix issues and add new features.',
        'В первые месяцы остаёмся рядом, исправляем ошибки и добавляем новые возможности.'),
    'Nazorat va rivojlantirish': ('Support and growth', 'Сопровождение и развитие'),

    # ---- Qadriyatlar
    "Tizim ishga tushguncha mas'uliyat bizda.": (
        "We're responsible until the system is up and running.", 'Отвечаем за результат, пока система не заработает.'),
    'Natija': ('Results', 'Результат'),
    "Texnik tilni biznes tiliga o'giramiz.": ('We translate tech talk into business language.', 'Переводим технический язык на язык бизнеса.'),
    'Tushunarlilik': ('Clarity', 'Понятность'),
    "Mijoz jamoasini o'qitamiz va yonida bo'lamiz.": ("We train the client's team and stay by their side.", 'Обучаем команду клиента и остаёмся рядом.'),
    'Hamkorlik': ('Partnership', 'Партнёрство'),

    # ---- Sozlamalar (sarlavhalar va matnlar)
    'Sohangizga mos yechim': ('Solutions for your industry', 'Решения для вашей отрасли'),
    'Ishlash tartibimiz': ('How we work', 'Как мы работаем'),
    'Har bir soha uchun tayyor modullar va amaliy tajriba.': (
        'Ready-made modules and hands-on experience for every industry.', 'Готовые модули и практический опыт для каждой отрасли.'),
    'Dasturni emas, ishlaydigan tizimni sotamiz': (
        "We don't sell software — we deliver systems that work", 'Мы продаём не программу, а работающую систему'),
    'Biznes va texnologiyani birga biladigan odamlar.': (
        'People who understand both business and technology.', 'Люди, которые разбираются и в бизнесе, и в технологиях.'),
    'Biz bilan ishlagan kompaniyalar va tashkilotlar.': (
        'Companies and organizations we have worked with.', 'Компании и организации, с которыми мы работали.'),
    '★ Rasmiy hamkorlar': ('★ Official partners', '★ Официальные партнёры'),
    "Ma'lumot qoldiring, 1 ish kuni ichida bog'lanamiz.": (
        'Leave your details and we will contact you within 1 business day.', 'Оставьте заявку — свяжемся в течение 1 рабочего дня.'),
    'МойСклад · amoCRM · Odoo rasmiy hamkori': ('Official MoySklad · amoCRM · Odoo partner', 'Официальный партнёр МойСклад · amoCRM · Odoo'),
    'Biz tizimlashtirgan bizneslar': ('Businesses we have systematized', 'Бизнесы, которые мы систематизировали'),
    'Biznesingizni *yagona tizimga* jamlaymiz': (
        'We bring your business into *one unified system*', 'Объединяем ваш бизнес в *единую систему*'),
    "Finora Systems — ERP, CRM va avtomatlashtirish bo'yicha mutaxassislar jamoasi. Hisob-kitobdan hisobotgacha hammasi bitta joyda.": (
        'Finora Systems is a team of ERP, CRM and automation experts. From accounting to reporting — everything in one place.',
        'Finora Systems — команда экспертов по ERP, CRM и автоматизации. От учёта до отчётности — всё в одном месте.'),
    'Bepul konsultatsiya': ('Free consultation', 'Бесплатная консультация'),
    'Jamoamiz mutaxassislari': ('Our team', 'Наша команда'),
    'IT yechimlar · ERP · Avtomatlashtirish': ('IT solutions · ERP · Automation', 'IT-решения · ERP · Автоматизация'),
    "Finora Systems — ERP, CRM va biznes avtomatlashtirish bo'yicha IT yechimlar. Jarayonni tartibga solamiz, tizimni quramiz va jamoani o'rgatamiz.": (
        'Finora Systems — IT solutions for ERP, CRM and business automation. We organize processes, build systems and train your team.',
        'Finora Systems — IT-решения для ERP, CRM и автоматизации бизнеса. Наводим порядок в процессах, строим систему и обучаем команду.'),
    "Farg'ona, O'zbekiston": ('Fergana, Uzbekistan', 'Фергана, Узбекистан'),
    "Finora Systems — ERP, CRM va biznes avtomatlashtirish bo'yicha IT yechimlar. Odoo, МойСклад va amoCRM rasmiy hamkori.": (
        'Finora Systems — IT solutions for ERP, CRM and business automation. Official Odoo, MoySklad and amoCRM partner.',
        'Finora Systems — IT-решения для ERP, CRM и автоматизации бизнеса. Официальный партнёр Odoo, МойСклад и amoCRM.'),
    'Hamkor mijozlar': ('Our clients', 'Наши клиенты'),
    'Biznes jarayonini ham, texnologiyani ham tushunamiz. Tizim sizning ishingizga moslanadi, aksincha emas.': (
        'We understand both business processes and technology. The system adapts to your work — not the other way around.',
        'Мы понимаем и бизнес-процессы, и технологии. Система подстраивается под вашу работу, а не наоборот.'),
    '8 bosqich: har biri hujjat yoki ishlaydigan natija bilan yopiladi.': (
        '8 stages, each closed with a document or a working result.', '8 этапов: каждый завершается документом или работающим результатом.'),
    "Biznesingizda vaqt va pul qayerda yo'qolayotganini topamiz": (
        "We'll find where your business is losing time and money", 'Найдём, где ваш бизнес теряет время и деньги'),
    "Ariza qoldiring, 1 ish kuni ichida o'zimiz qo'ng'iroq qilamiz. Ma'lumotlaringiz sir saqlanadi.": (
        "Leave a request and we'll call you within 1 business day. Your data stays confidential.",
        'Оставьте заявку — перезвоним в течение 1 рабочего дня. Ваши данные конфиденциальны.'),
}

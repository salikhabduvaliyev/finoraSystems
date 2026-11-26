"""Finora Systems — sayt kontenti modellari.

"Qatorlar" maydonlari (punktlar, teglar va h.k.) oddiy matn sifatida saqlanadi:
har bir qator — alohida punkt. Shablonda `|lines` filtri bilan ro'yxatga aylanadi.
"""
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from .media import parse_video, slugify_uz

LINES_HELP = 'Har bir qator — alohida punkt'
IMG_HELP = "Yuklansa, tayyor illyustratsiya o'rniga shu rasm chiqadi (400×230 nisbat)."

MOCK_CHOICES = [
    ('savdo', 'Savdo va ombor'), ('ishlab', 'Ishlab chiqarish'), ('talim', "Ta'lim"),
    ('klinika', 'Klinika'), ('turizm', 'Turizm'), ('transport', 'Transport'),
    ('energiya', 'Energetika'), ('mulk', "Ko'chmas mulk"),
]

video_file_validator = FileExtensionValidator(['mp4', 'webm', 'mov'])


def lines(value):
    return [s.strip() for s in str(value or '').splitlines() if s.strip()]


class Ordered(models.Model):
    sort = models.PositiveIntegerField('Tartib', default=0, help_text="Kichik raqam yuqorida chiqadi")
    active = models.BooleanField("Saytda ko'rsatish", default=True)

    class Meta:
        abstract = True
        ordering = ['sort', 'id']


# ---------------------------------------------------------------- Xizmatlar va sohalar

class Service(Ordered):
    title = models.CharField('Nomi', max_length=200)
    subtitle = models.CharField('Qisqa izoh', max_length=200, blank=True, help_text='Masalan: Odoo va МойСклад')
    items = models.TextField('Punktlar', blank=True, help_text=LINES_HELP)
    description = models.TextField('Batafsil tavsif (xizmat sahifasi uchun)', blank=True,
                                   help_text="Xatboshilarni bo'sh qator bilan ajrating")
    image = models.ImageField('Muqova rasmi (ixtiyoriy)', upload_to='services/', blank=True,
                              help_text="Xizmat sahifasining o'ng tomonida chiqadi")
    in_footer = models.BooleanField("Footerda ko'rsatish", default=True)

    class Meta(Ordered.Meta):
        verbose_name = 'xizmat'
        verbose_name_plural = 'Xizmatlar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk, 'slug': slugify_uz(self.title)})


class Industry(Ordered):
    title = models.CharField('Soha nomi', max_length=200)
    label = models.CharField('Kichik yorliq', max_length=100, blank=True)
    short = models.TextField('Qisqa tavsif', blank=True)
    mock = models.CharField('Illyustratsiya', max_length=20, choices=MOCK_CHOICES, default='savdo')
    image = models.ImageField('Rasm (ixtiyoriy)', upload_to='industries/', blank=True, help_text=IMG_HELP)
    pains = models.TextField("Og'riq nuqtalari", blank=True, help_text=LINES_HELP)
    solutions = models.TextField('Bizning yechim', blank=True, help_text=LINES_HELP)
    ai = models.TextField('AI yechim', blank=True)
    web = models.TextField('Veb-sayt yechimi', blank=True)
    description = models.TextField('Batafsil tavsif (soha sahifasi uchun)', blank=True,
                                   help_text="Xatboshilarni bo'sh qator bilan ajrating")
    on_home = models.BooleanField("Bosh sahifada ko'rsatish", default=True)
    in_footer = models.BooleanField("Footerda ko'rsatish", default=False)

    class Meta(Ordered.Meta):
        verbose_name = 'soha'
        verbose_name_plural = 'Sohalar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('industry_detail', kwargs={'pk': self.pk, 'slug': slugify_uz(self.title)})


# ---------------------------------------------------------------- Keyslar

class Case(Ordered):
    title = models.CharField('Sarlavha', max_length=250)
    client = models.CharField('Mijoz nomi', max_length=150, blank=True)
    logo = models.ImageField('Mijoz logotipi', upload_to='cases/logos/', blank=True,
                             help_text="Bo'lmasa, mijoz nomi matn ko'rinishida chiqadi")
    description = models.TextField('Qisqa tavsif', blank=True, help_text='Kartochkada va keys sahifasi boshida chiqadi')
    direction = models.CharField("Yo'nalish", max_length=150, blank=True)
    industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True, blank=True, related_name='cases',
                                 verbose_name='Soha', help_text="Keys shu soha sahifasida ko'rsatiladi")
    tags = models.TextField('Teglar', blank=True, help_text='Har bir qator — alohida teg (Odoo 19, ERP …)')
    year = models.CharField('Yil', max_length=20, blank=True)
    duration = models.CharField('Muddat', max_length=50, blank=True, help_text='Masalan: 3 oy')
    result = models.CharField('Qisqa natija (kartochka uchun)', max_length=200, blank=True)
    mock = models.CharField('Illyustratsiya', max_length=20, choices=MOCK_CHOICES, default='savdo')
    image = models.ImageField('Muqova rasmi (ixtiyoriy)', upload_to='cases/', blank=True, help_text=IMG_HELP)
    on_home = models.BooleanField("Bosh sahifa karuselida ko'rsatish", default=False)

    challenge = models.TextField('Vazifa / muammo', blank=True, help_text="Xatboshilarni bo'sh qator bilan ajrating")
    solution = models.TextField('Yechim', blank=True, help_text="Xatboshilarni bo'sh qator bilan ajrating")
    works = models.TextField('Bajarilgan ishlar', blank=True, help_text=LINES_HELP)
    metrics = models.TextField('Natija raqamlari', blank=True,
                               help_text='Har qatorda: qiymat | izoh. Masalan: 40% | tezroq hisobot')

    t_text = models.TextField('Otziv matni', blank=True)
    t_author = models.CharField('Kim aytgan (ism)', max_length=150, blank=True)
    t_role = models.CharField('Lavozimi', max_length=150, blank=True, help_text='Masalan: Direktor, Kerama City')
    t_photo = models.ImageField('Foto', upload_to='cases/testimonials/', blank=True)
    t_video_url = models.CharField('Video-otziv havolasi', max_length=300, blank=True,
                                   help_text='YouTube, Instagram (Reels yoki post) yoki Vimeo havolasi')
    t_video_file = models.FileField('yoki video fayl', upload_to='cases/videos/', blank=True,
                                    validators=[video_file_validator], help_text='MP4, WEBM yoki MOV')

    class Meta(Ordered.Meta):
        verbose_name = 'keys'
        verbose_name_plural = 'Keyslar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('case_detail', kwargs={'pk': self.pk, 'slug': slugify_uz(self.title)})

    def clean(self):
        if self.t_video_url and not parse_video(self.t_video_url):
            raise ValidationError({'t_video_url': 'YouTube, Instagram yoki Vimeo havolasini kiriting.'})

    @property
    def testimonial_video(self):
        return self.t_video_file.url if self.t_video_file else self.t_video_url

    @property
    def metric_list(self):
        out = []
        for line in lines(self.metrics):
            value, _, text = line.partition('|')
            out.append({'value': value.strip(), 'text': text.strip()})
        return out


class VideoBase(models.Model):
    title = models.CharField('Nomi', max_length=200, blank=True, help_text="Kartochkada ko'rinadi")
    url = models.CharField('Video havolasi', max_length=300, blank=True,
                           help_text='YouTube, Instagram (Reels yoki post) yoki Vimeo havolasi')
    file = models.FileField('yoki video fayl', upload_to='videos/', blank=True, validators=[video_file_validator],
                            help_text="MP4, WEBM yoki MOV. Katta videolarni YouTube'ga joylab havolasini qo'ying.")
    cover = models.ImageField('Muqova (ixtiyoriy)', upload_to='videos/covers/', blank=True,
                              help_text="Instagram va yuklangan videolar uchun tavsiya etiladi (YouTube'da avtomatik)")
    sort = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        abstract = True
        ordering = ['sort', 'id']
        verbose_name = 'video'
        verbose_name_plural = 'Videolar'

    def clean(self):
        if not self.url and not self.file:
            raise ValidationError('Havola kiriting yoki video fayl yuklang.')
        if self.url and not parse_video(self.url):
            raise ValidationError({'url': 'YouTube, Instagram yoki Vimeo havolasini kiriting.'})

    @property
    def src(self):
        return self.file.url if self.file else self.url

    @property
    def info(self):
        return parse_video(self.src)

    def __str__(self):
        return self.url or (self.file.name if self.file else 'video')


class ImageBase(models.Model):
    image = models.ImageField('Rasm', upload_to='gallery/')
    sort = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        abstract = True
        ordering = ['sort', 'id']
        verbose_name = 'rasm'
        verbose_name_plural = 'Rasmlar galereyasi'

    def __str__(self):
        return self.image.name


class CaseVideo(VideoBase):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='videos')

    class Meta(VideoBase.Meta):
        pass


class CaseImage(ImageBase):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='images')

    class Meta(ImageBase.Meta):
        pass


class ServiceVideo(VideoBase):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='videos')

    class Meta(VideoBase.Meta):
        pass


class IndustryVideo(VideoBase):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='videos')

    class Meta(VideoBase.Meta):
        pass


class IndustryImage(ImageBase):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='images')

    class Meta(ImageBase.Meta):
        pass


doc_validator = FileExtensionValidator(['pdf', 'ppt', 'pptx'])


class Presentation(models.Model):
    """Xizmat taqdimoti: PDF ko'rish oynasida ochiladi, PPT/PPTX yuklab olinadi, yoki tashqi havola (Google Slides, Canva)."""
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True, related_name='presentations',
                                verbose_name='Xizmat')
    title = models.CharField('Nomi', max_length=200)
    file = models.FileField('Fayl (PDF, PPT, PPTX)', upload_to='presentations/', blank=True, validators=[doc_validator],
                            help_text="PDF saytda to'g'ridan-to'g'ri ochiladi")
    url = models.URLField('yoki havola', blank=True, help_text='Google Slides, Canva va h.k.')
    sort = models.PositiveIntegerField('Tartib', default=0)

    class Meta:
        ordering = ['sort', 'id']
        verbose_name = 'taqdimot'
        verbose_name_plural = 'Taqdimotlar'

    def __str__(self):
        return self.title

    def clean(self):
        if not self.file and not self.url:
            raise ValidationError('Fayl yuklang yoki havola kiriting.')

    @property
    def is_pdf(self):
        return bool(self.file) and self.file.name.lower().endswith('.pdf')

    @property
    def ext(self):
        return self.file.name.rsplit('.', 1)[-1].upper() if self.file else ''

    @property
    def embed_url(self):
        """Google Slides havolasini sahifaga joylash ko'rinishiga keltirish."""
        u = self.url or ''
        if 'docs.google.com/presentation' in u:
            return u.split('/edit')[0].split('/pub')[0].rstrip('/') + '/embed'
        if 'canva.com/design' in u and '/view' in u:
            return u.split('?')[0] + '?embed'
        return ''


# ---------------------------------------------------------------- Jamoa

class TeamMember(Ordered):
    name = models.CharField('Ism familiya', max_length=150)
    role = models.CharField('Lavozim', max_length=150, blank=True)
    photo = models.ImageField('Foto', upload_to='team/', blank=True, help_text='Kvadrat rasm tavsiya etiladi')
    on_home = models.BooleanField("Bosh sahifada ko'rsatish", default=True)
    intro = models.TextField('Qisqa tanishtiruv', blank=True, help_text='Ism ostida chiqadigan 1–2 gap')
    bio = models.TextField('Batafsil biografiya', blank=True, help_text="Xatboshilarni bo'sh qator bilan ajrating")
    skills = models.TextField("Ko'nikmalar", blank=True, help_text='Har bir qator — alohida teg')
    experience = models.TextField('Tajriba', blank=True, help_text=LINES_HELP)
    education = models.TextField("Ta'lim", blank=True, help_text=LINES_HELP)
    achievements = models.TextField('Sertifikat va yutuqlar', blank=True, help_text=LINES_HELP)
    telegram = models.CharField('Telegram', max_length=150, blank=True, help_text='@username yoki havola')
    linkedin = models.URLField('LinkedIn havola', blank=True)
    instagram = models.URLField('Instagram havola', blank=True)
    email = models.EmailField('Email', blank=True)

    class Meta(Ordered.Meta):
        verbose_name = "jamoa a'zosi"
        verbose_name_plural = 'Jamoa'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member_detail', kwargs={'pk': self.pk, 'slug': slugify_uz(self.name)})


class MemberVideo(VideoBase):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='videos')

    class Meta(VideoBase.Meta):
        pass


class MemberImage(ImageBase):
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='images')

    class Meta(ImageBase.Meta):
        pass


# ---------------------------------------------------------------- Bosh sahifa bloklari

class Client(Ordered):
    name = models.CharField('Kompaniya nomi', max_length=150)
    logo = models.ImageField('Logotip', upload_to='clients/')
    dark = models.BooleanField("To'q fonda ko'rsatish", default=False, help_text='Oq logotiplar uchun')
    row = models.CharField('Lenta qatori', max_length=1, choices=[('1', '1-qator'), ('2', '2-qator (teskari)')], default='1')

    class Meta(Ordered.Meta):
        verbose_name = 'mijoz logotipi'
        verbose_name_plural = 'Mijozlar logotiplari'

    def __str__(self):
        return self.name


class Partner(Ordered):
    name = models.CharField('Nomi', max_length=100)
    logo = models.ImageField('Logotip', upload_to='partners/', blank=True)
    color = models.CharField("Matn rangi (logotip bo'lmasa)", max_length=7, default='#0b5ed7')

    class Meta(Ordered.Meta):
        verbose_name = 'rasmiy hamkor'
        verbose_name_plural = 'Rasmiy hamkorlar'

    def __str__(self):
        return self.name


class Stat(Ordered):
    ICONS = [('b', 'Ustunlar'), ('t', "Vaqt chizig'i"), ('c', 'Grafik'), ('g', 'Nishon')]
    value = models.CharField('Qiymat', max_length=30, help_text="Raqam bilan boshlansa animatsiya bo'ladi: 100+, 6 yil")
    label = models.CharField('Izoh', max_length=100, blank=True)
    icon = models.CharField('Ikon', max_length=1, choices=ICONS, default='b')
    highlight = models.BooleanField("Ajratib ko'rsatish", default=False)

    class Meta(Ordered.Meta):
        verbose_name = 'raqam'
        verbose_name_plural = 'Raqamlar'

    def __str__(self):
        return f'{self.value} — {self.label}'


class WhyCard(Ordered):
    ICONS = [('0', 'Odam'), ('1', 'Ustunlar'), ('2', 'Kalitlar')]
    title = models.CharField('Sarlavha', max_length=150)
    text = models.TextField('Matn', blank=True)
    icon = models.CharField('Ikon', max_length=1, choices=ICONS, default='0')

    class Meta(Ordered.Meta):
        verbose_name = 'karta'
        verbose_name_plural = 'Nega Finora'

    def __str__(self):
        return self.title


class Step(Ordered):
    title = models.CharField('Bosqich nomi', max_length=150)
    text = models.TextField('Tavsif', blank=True)

    class Meta(Ordered.Meta):
        verbose_name = 'bosqich'
        verbose_name_plural = 'Ish jarayoni'

    def __str__(self):
        return self.title


class Value(Ordered):
    title = models.CharField('Sarlavha', max_length=150)
    text = models.TextField('Matn', blank=True)

    class Meta(Ordered.Meta):
        verbose_name = 'qadriyat'
        verbose_name_plural = 'Qadriyatlar'

    def __str__(self):
        return self.title


# ---------------------------------------------------------------- Arizalar

class Lead(models.Model):
    STATUS = [('new', 'Yangi'), ('progress', 'Jarayonda'), ('done', 'Yakunlandi'), ('spam', 'Spam')]
    SOURCES = {'cta': 'Sahifa pastidagi ariza bloki', 'aloqa': 'Aloqa sahifasi'}

    name = models.CharField('Ism', max_length=80)
    phone = models.CharField('Telefon', max_length=30)
    service = models.CharField('Xizmat', max_length=150, blank=True)
    message = models.TextField('Xabar', blank=True)
    source = models.CharField('Manba', max_length=30, blank=True)
    page = models.CharField('Sahifa', max_length=300, blank=True)
    lang = models.CharField('Til', max_length=5, blank=True)
    status = models.CharField('Holat', max_length=10, choices=STATUS, default='new')
    note = models.TextField('Ichki izoh', blank=True, help_text='Faqat adminlar ko‘radi')
    created_at = models.DateTimeField('Sana', auto_now_add=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'ariza'
        verbose_name_plural = 'Arizalar'

    def __str__(self):
        return f'{self.name} · {self.phone}'

    @property
    def source_label(self):
        return self.SOURCES.get(self.source, self.source or 'Sayt')


# ---------------------------------------------------------------- Sozlamalar (yagona yozuv)

class SiteSettings(models.Model):
    site_name = models.CharField('Sayt nomi', max_length=100, default='Finora Systems')
    logo = models.ImageField('Logotip', upload_to='site/', blank=True, help_text="To'q fon uchun PNG. Bo'sh bo'lsa standart logo")
    meta_description = models.TextField('SEO tavsif (Google uchun)', blank=True)
    phone = models.CharField('Telefon', max_length=50, blank=True)
    email = models.CharField('Email', max_length=100, blank=True)
    address = models.CharField('Manzil', max_length=200, blank=True)
    telegram_username = models.CharField('Telegram (username)', max_length=100, blank=True)

    social_telegram = models.CharField('Telegram', max_length=200, blank=True, help_text='@username yoki havola')
    social_instagram = models.CharField('Instagram havola', max_length=200, blank=True)
    social_linkedin = models.CharField('LinkedIn havola', max_length=200, blank=True)
    social_youtube = models.CharField('YouTube havola', max_length=200, blank=True)
    social_facebook = models.CharField('Facebook havola', max_length=200, blank=True)

    hero_tag = models.CharField('Yuqori yorliq', max_length=200, blank=True)
    hero_title = models.CharField('Asosiy sarlavha', max_length=200, blank=True,
                                  help_text="*yulduzcha* ichidagi so'zlar rangli chiqadi")
    hero_lead = models.TextField('Sarlavha osti matni', blank=True)
    partners_label = models.CharField('Hamkorlar lentasi yozuvi', max_length=100, blank=True)

    why_title = models.CharField('Nega Finora — sarlavha', max_length=200, blank=True)
    why_sub = models.TextField('Nega Finora — izoh', blank=True)
    ind_title = models.CharField('Sohalar — sarlavha', max_length=200, blank=True)
    ind_sub = models.TextField('Sohalar — izoh', blank=True)
    cases_title = models.CharField('Keyslar — sarlavha', max_length=200, blank=True)
    clients_title = models.CharField('Mijozlar — sarlavha', max_length=200, blank=True)
    clients_sub = models.TextField('Mijozlar — izoh', blank=True)
    steps_title = models.CharField('Jarayon — sarlavha', max_length=200, blank=True)
    steps_sub = models.TextField('Jarayon — izoh', blank=True)
    team_title = models.CharField('Jamoa — sarlavha', max_length=200, blank=True)
    team_sub = models.TextField('Jamoa — izoh', blank=True)

    cta_title = models.CharField('Ariza bloki — sarlavha', max_length=200, blank=True)
    cta_text = models.TextField('Ariza bloki — matn', blank=True)

    founder_name = models.CharField('Asoschi — ism familiya', max_length=150, blank=True)
    founder_bio = models.TextField('Asoschi — qisqa biografiya', blank=True)
    founder_education = models.TextField("Asoschi — ta'lim", blank=True, help_text=LINES_HELP)
    founder_experience = models.TextField('Asoschi — tajriba', blank=True, help_text=LINES_HELP)
    founder_expertise = models.TextField('Asoschi — ekspertiza teglari', blank=True, help_text='Har bir qator — alohida teg')

    footer_about = models.TextField('Footer — kompaniya haqida', blank=True)
    footer_bottom = models.CharField("Footer — pastki o'ng yozuv", max_length=200, blank=True)

    tg_bot_token = models.CharField('Telegram bot token', max_length=200, blank=True,
                                    help_text="@BotFather'dan olingan token. Yangi ariza kelganda shu bot xabar yuboradi.")
    tg_chat_id = models.TextField('Chat ID(lar)', blank=True,
                                  help_text="Har birini yangi qatorda yoki vergul bilan yozing. Guruhlar -100… bilan boshlanadi.")

    class Meta:
        verbose_name = 'sayt sozlamalari'
        verbose_name_plural = 'Sayt sozlamalari'

    def __str__(self):
        return 'Sayt sozlamalari'

    def save(self, *args, **kwargs):
        self.pk = 1  # har doim bitta yozuv
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

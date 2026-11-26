from django.conf import settings
from django.urls import reverse, translate_url
from django.utils import translation
from django.utils.translation import get_language, gettext as _

from .models import Industry, Service, SiteSettings

SOCIAL_NAMES = [('telegram', 'Telegram'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'),
                ('youtube', 'YouTube'), ('facebook', 'Facebook')]

# Menyu bandi -> qaysi sahifalar unga tegishli (faol holat uchun)
NAV = [('home', ('home',)), ('services', ('services', 'service_detail')), ('industries', ('industries', 'industry_detail')),
       ('cases', ('cases', 'case_detail')), ('team', ('team', 'member_detail')), ('contact', ('contact',))]

LANG_SHORT = {'uz': 'UZ', 'en': 'EN', 'ru': 'RU'}


def nav_labels():
    return {'home': _('Bosh sahifa'), 'services': _('Xizmatlar'), 'industries': _('Sohalar'),
            'cases': _('Keyslar'), 'team': _('Jamoa'), 'contact': _('Aloqa')}


def social_url(kind, value):
    v = str(value or '').strip()
    if not v:
        return ''
    if v.startswith(('http://', 'https://')):
        return v
    if kind == 'telegram':
        return 'https://t.me/' + v.lstrip('@')
    if kind == 'instagram':
        return 'https://www.instagram.com/' + v.lstrip('@')
    return ''


def lang_url(request, path, code):
    """Joriy sahifaning boshqa tildagi manzili. Keys/a'zo sahifalarida slug ham o'sha tilda bo'ladi."""
    match = request.resolver_match
    if match and match.url_name in ('case_detail', 'member_detail', 'industry_detail', 'service_detail'):
        from .models import Case, Industry, Service, TeamMember  # noqa: PLC0415
        model = {'case_detail': Case, 'member_detail': TeamMember, 'industry_detail': Industry,
                 'service_detail': Service}[match.url_name]
        obj = model.objects.filter(pk=match.kwargs.get('pk'), active=True).first()
        if obj:
            with translation.override(code):
                return obj.get_absolute_url()
    return translate_url(path, code)


def site_context(request):
    """Har bir sayt sahifasiga sozlamalar, menyu, tillar va footer ma'lumotlari."""
    if request.path.startswith('/admin'):
        return {}
    s = SiteSettings.load()
    current = getattr(request.resolver_match, 'url_name', None)
    labels = nav_labels()
    lang = get_language()
    path = request.get_full_path()
    languages = [{'code': code, 'short': LANG_SHORT.get(code, code.upper()), 'name': name,
                  'url': lang_url(request, path, code), 'on': code == lang} for code, name in settings.LANGUAGES]
    socials = [(k, n, social_url(k, getattr(s, 'social_' + k))) for k, n in SOCIAL_NAMES]
    return {
        's': s,
        'nav': [(reverse(name), labels[name], current in names) for name, names in NAV],
        'languages': languages,
        'all_services': Service.objects.filter(active=True),
        'footer_services': Service.objects.filter(active=True, in_footer=True),
        'footer_industries': Industry.objects.filter(active=True, in_footer=True),
        'socials': [x for x in socials if x[2]],
        'tg_handle': str(s.telegram_username or '').strip().lstrip('@'),
        'logo_url': s.logo.url if s.logo else '/static/img/logo.png',
        'js_t': {
            'sending': _('Yuborilmoqda…'),
            'name_err': _('Ismingizni yozing — kimga qo‘ng‘iroq qilishni bilishimiz uchun.'),
            'phone_err': _('Telefon raqamini to‘liq yozing, masalan: 90 123-45-67.'),
            'net_err': _('Ariza yuborilmadi — internet aloqasini tekshirib, qayta urinib ko‘ring.'),
            'ok_title': _('Rahmat! Arizangiz qabul qilindi.'),
            'ok_text': _('1 ish kuni ichida siz bilan bog‘lanamiz.'),
            'close': _('Yopish'),
        },
    }

from .models import Industry, Service, SiteSettings

NAV = [('/', 'Bosh sahifa'), ('/xizmatlar', 'Xizmatlar'), ('/sohalar', 'Sohalar'),
       ('/keyslar', 'Keyslar'), ('/jamoa', 'Jamoa'), ('/aloqa', 'Aloqa')]

SOCIAL_NAMES = [('telegram', 'Telegram'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'),
                ('youtube', 'YouTube'), ('facebook', 'Facebook')]


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


def site_context(request):
    """Har bir sayt sahifasiga sozlamalar, menyu va footer ma'lumotlari."""
    if request.path.startswith('/admin'):
        return {}
    s = SiteSettings.load()
    path = request.path.rstrip('/') or '/'
    section = '/' + path.strip('/').split('/')[0] if path != '/' else '/'
    socials = [(k, n, social_url(k, getattr(s, 'social_' + k))) for k, n in SOCIAL_NAMES]
    return {
        's': s,
        'nav': [(href, label, href == section) for href, label in NAV],
        'all_services': Service.objects.filter(active=True),
        'footer_services': Service.objects.filter(active=True, in_footer=True),
        'footer_industries': Industry.objects.filter(active=True, in_footer=True),
        'socials': [x for x in socials if x[2]],
        'tg_handle': str(s.telegram_username or '').strip().lstrip('@'),
        'logo_url': s.logo.url if s.logo else '/static/img/logo.png',
    }

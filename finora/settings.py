"""Finora Systems — Django sozlamalari.

Maxfiy qiymatlar loyiha ildizidagi .env faylidan (yoki muhit o'zgaruvchilaridan) o'qiladi.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _load_env(path):
    """Oddiy .env o'quvchi: KALIT=qiymat qatorlari (qo'shimcha kutubxonasiz)."""
    if not path.exists():
        return
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=', 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_env(BASE_DIR / '.env')

DEBUG = os.environ.get('DJANGO_DEBUG', '0') == '1'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')
if not SECRET_KEY:
    if not DEBUG:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(".env faylida DJANGO_SECRET_KEY yo'q. README'dagi 3-qadamni bajaring.")
    SECRET_KEY = 'dev-only-insecure-key'
ALLOWED_HOSTS = [h.strip() for h in os.environ.get(
    'DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,.pythonanywhere.com').split(',') if h.strip()]
CSRF_TRUSTED_ORIGINS = [o.strip() for o in os.environ.get('DJANGO_CSRF_ORIGINS', '').split(',') if o.strip()]

INSTALLED_APPS = [
    'modeltranslation',  # ko'p tilli kontent — django.contrib.admin dan oldin bo'lishi shart
    'core',  # admin shablonlarini almashtirish uchun django.contrib.admin dan oldin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',  # admin panelga parol terib kirishdan himoya
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'core.middleware.AdminUzbekMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',  # ro'yxatda oxirgi bo'lishi kerak
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',  # birinchi bo'lishi kerak
    'django.contrib.auth.backends.ModelBackend',
]

# ---- django-axes: noto'g'ri parol urinishlarini cheklash
AXES_FAILURE_LIMIT = 5                     # 5 ta noto'g'ri urinishdan keyin…
AXES_COOLOFF_TIME = 1                      # …1 soatga bloklanadi
AXES_LOCKOUT_PARAMETERS = ['ip_address']   # IP manzil bo'yicha bloklash
AXES_RESET_ON_SUCCESS = True               # to'g'ri kirilsa, hisob nolga tushadi
AXES_CLIENT_IP_CALLABLE = 'core.ip.client_ip'
AXES_LOCKOUT_TEMPLATE = 'axes_lockout.html'

ROOT_URLCONF = 'finora.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'core.context.site_context',
    ]},
}]

WSGI_APPLICATION = 'finora.wsgi.application'

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.environ.get('DJANGO_DB_PATH') or BASE_DIR / 'db.sqlite3',
}}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
]

LANGUAGE_CODE = 'uz'
LANGUAGES = [
    ('uz', "O'zbekcha"),
    ('en', 'English'),
    ('ru', 'Русский'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

# django-modeltranslation: kontent maydonlari har bir til uchun alohida
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('uz',)  # tarjima bo'sh bo'lsa — o'zbekchasi chiqadi
# Admin'dagi UZ/EN/RU yorliqlari uchun jQuery UI — tashqi CDN'siz, loyihaning o'zidan
JQUERY_UI_URL = '/static/vendor/jquery-ui.min.js'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'  # collectstatic shu yerga yig'adi (PythonAnywhere uchun)

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Video yuklash uchun katta so'rovlar
DATA_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 5 * 1024 * 1024

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
APPEND_SLASH = True

CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'SAMEORIGIN'
if not DEBUG:
    SESSION_COOKIE_SECURE = os.environ.get('DJANGO_HTTPS', '1') == '1'
    CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {'console': {'class': 'logging.StreamHandler'}},
    'loggers': {'core': {'handlers': ['console'], 'level': 'INFO'}},
}

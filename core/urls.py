from django.urls import path, re_path
from django.utils.text import format_lazy
from django.utils.translation import pgettext_lazy

from . import views


def seg(word):
    """URL bo'lagi har bir tilda o'zicha: /xizmatlar, /en/services, /ru/uslugi."""
    return pgettext_lazy('url', word)


DETAIL = r'/(?P<pk>\d+)(?:-(?P<slug>[\w-]*))?/?$'

# Til prefiksi bilan ishlaydigan sahifalar (finora/urls.py dagi i18n_patterns ichida)
site_patterns = [
    path('', views.home, name='home'),
    re_path(format_lazy('^{}/?$', seg('xizmatlar')), views.services, name='services'),
    re_path(format_lazy('^{}' + DETAIL, seg('xizmatlar')), views.service_detail, name='service_detail'),
    re_path(format_lazy('^{}/?$', seg('sohalar')), views.industries, name='industries'),
    re_path(format_lazy('^{}' + DETAIL, seg('sohalar')), views.industry_detail, name='industry_detail'),
    re_path(format_lazy('^{}/?$', seg('keyslar')), views.cases, name='cases'),
    re_path(format_lazy('^{}' + DETAIL, seg('keyslar')), views.case_detail, name='case_detail'),
    re_path(format_lazy('^{}/?$', seg('jamoa')), views.team, name='team'),
    re_path(format_lazy('^{}' + DETAIL, seg('jamoa')), views.member_detail, name='member_detail'),
    re_path(format_lazy('^{}/?$', seg('aloqa')), views.contact, name='contact'),
]

# Tilga bog'liq bo'lmagan manzillar
plain_patterns = [
    path('api/lead', views.api_lead, name='api_lead'),
    path('robots.txt', views.robots),
]

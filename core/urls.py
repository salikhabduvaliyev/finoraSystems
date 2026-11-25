from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^xizmatlar/?$', views.services, name='services'),
    re_path(r'^sohalar/?$', views.industries, name='industries'),
    re_path(r'^keyslar/?$', views.cases, name='cases'),
    re_path(r'^keyslar/(?P<pk>\d+)(?:-(?P<slug>[\w-]*))?/?$', views.case_detail, name='case_detail'),
    re_path(r'^jamoa/?$', views.team, name='team'),
    re_path(r'^jamoa/(?P<pk>\d+)(?:-(?P<slug>[\w-]*))?/?$', views.member_detail, name='member_detail'),
    re_path(r'^aloqa/?$', views.contact, name='contact'),
    path('api/lead', views.api_lead, name='api_lead'),
    path('robots.txt', views.robots),
]

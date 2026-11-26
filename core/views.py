import json
import re
from urllib.parse import urlparse

from django.core.cache import cache
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.utils import translation
from django.utils.translation import gettext as _
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .media import slugify_uz
from .models import (Case, Client, Industry, Lead, Partner, Presentation, Service, ServiceVideo, Stat, Step,
                     TeamMember, Value, WhyCard)
from .notify import notify_lead


def active(model):
    return model.objects.filter(active=True)


def home(request):
    clients = list(active(Client))
    return render(request, 'site/home.html', {
        'stats': active(Stat),
        'partners': active(Partner),
        'why': active(WhyCard),
        'industries': active(Industry).filter(on_home=True),
        'carousel': active(Case).filter(on_home=True),
        'clients_row1': [c for c in clients if c.row != '2'],
        'clients_row2': [c for c in clients if c.row == '2'],
        'steps': active(Step),
        'team': active(TeamMember).filter(on_home=True),
    })


def services(request):
    return render(request, 'site/services.html',
                  {'services': active(Service).prefetch_related('presentations', 'videos')})


def service_detail(request, pk, slug=''):
    obj = active(Service).filter(pk=pk).first()
    if not obj:
        raise Http404
    if slug != slugify_uz(obj.title):
        return redirect(obj.get_absolute_url(), permanent=True)
    return render(request, 'site/service_detail.html', {
        'obj': obj,
        'presentations': obj.presentations.all(),
        'videos': obj.videos.all(),
        'others': active(Service).exclude(pk=pk)[:3],
    })


def industries(request):
    return render(request, 'site/industries.html', {'industries': active(Industry)})


def cases(request):
    return render(request, 'site/cases.html', {'cases': active(Case)})


def team(request):
    return render(request, 'site/team.html', {'team': active(TeamMember), 'values': active(Value)})


def contact(request):
    return render(request, 'site/contact.html')


def _detail(request, model, pk, slug, template, name_attr):
    obj = active(model).filter(pk=pk).first()
    if not obj:
        raise Http404
    if slug != slugify_uz(getattr(obj, name_attr)):
        return redirect(obj.get_absolute_url(), permanent=True)
    others = active(model).exclude(pk=pk)
    return render(request, template, {'obj': obj, 'others': others[:3 if model is Case else 4]})


def industry_detail(request, pk, slug=''):
    obj = active(Industry).filter(pk=pk).first()
    if not obj:
        raise Http404
    if slug != slugify_uz(obj.title):
        return redirect(obj.get_absolute_url(), permanent=True)
    return render(request, 'site/industry_detail.html', {
        'obj': obj,
        'cases': obj.cases.filter(active=True),
        'others': active(Industry).exclude(pk=pk)[:3],
    })


def case_detail(request, pk, slug=''):
    obj = active(Case).filter(pk=pk).first()
    if not obj:
        raise Http404
    if slug != slugify_uz(obj.title):
        return redirect(obj.get_absolute_url(), permanent=True)
    # Oldingi / keyingi keys va undan keyingilari (ro'yxat aylanma: oxiridan boshiga qaytadi)
    items = list(active(Case))
    idx = next(i for i, c in enumerate(items) if c.pk == obj.pk)
    n = len(items)
    following = [items[(idx + k) % n] for k in range(1, min(n, 4))]
    return render(request, 'site/case_detail.html', {
        'obj': obj,
        'prev_case': items[idx - 1] if n > 1 else None,
        'next_case': items[(idx + 1) % n] if n > 1 else None,
        'others': following,
    })


def member_detail(request, pk, slug=''):
    return _detail(request, TeamMember, pk, slug, 'site/member_detail.html', 'name')


def page_not_found(request, exception=None):
    return render(request, 'site/404.html', status=404)


def robots(request):
    from django.http import HttpResponse
    return HttpResponse('User-agent: *\nDisallow: /admin/\n', content_type='text/plain')


# ---------------------------------------------------------------- Ariza qabul qilish

from .ip import client_ip as _client_ip


def _rate_limited(ip, limit=5, window=600):
    key = f'lead-rl:{ip}'
    n = cache.get(key, 0) + 1
    cache.set(key, n, window)
    return n > limit


@csrf_exempt  # ochiq forma: login bilan bog'liq emas; spamdan honeypot va IP limiti himoya qiladi
@require_POST
def api_lead(request):
    try:
        data = json.loads(request.body or b'{}')
    except ValueError:
        return JsonResponse({'error': _("So'rov noto'g'ri.")}, status=400)
    clip = lambda k, n: str(data.get(k) or '').strip()[:n]
    lang = clip('lang', 5) if clip('lang', 5) in {'uz', 'en', 'ru'} else 'uz'
    with translation.override(lang):
        return _save_lead(request, data, clip, lang)


def _save_lead(request, data, clip, lang):

    if data.get('website'):  # bot to'ldirgan yashirin maydon
        return JsonResponse({'ok': True})
    if _rate_limited(_client_ip(request)):
        return JsonResponse({'error': _("Juda ko'p ariza yuborildi. Birozdan keyin qayta urinib ko'ring yoki bizga qo'ng'iroq qiling.")}, status=429)

    name, phone = clip('name', 80), clip('phone', 20)
    digits = re.sub(r'\D', '', phone)
    if not name:
        return JsonResponse({'error': _('Ismingizni yozing.')}, status=400)
    if len(digits) < 9:
        return JsonResponse({'error': _("Telefon raqamini to'liq yozing, masalan: 90 123-45-67.")}, status=400)
    if len(digits) == 9:
        phone = '+998 ' + phone
    elif not phone.startswith('+'):
        phone = '+' + phone

    referer = urlparse(request.META.get('HTTP_REFERER', '')).path[:300]
    lead = Lead.objects.create(name=name, phone=phone, service=clip('service', 150), message=clip('message', 2000),
                               source=clip('source', 30), page=referer, lang=lang)
    notify_lead(lead)
    return JsonResponse({'ok': True})

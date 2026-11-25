from django import template
from django.db.models import Count
from django.urls import reverse

from ..models import (Case, Client, Industry, Lead, Partner, Service, Stat, Step, TeamMember, Value, WhyCard)

register = template.Library()

# Admin menyusidagi kontent bo'limlari (tartib bilan)
CONTENT = [Service, Industry, Case, TeamMember, Client, Partner, Stat, WhyCard, Step, Value]


def _changelist(model):
    return reverse(f'admin:core_{model._meta.model_name}_changelist')


@register.simple_tag
def admin_stats():
    counts = {r['status']: r['n'] for r in Lead.objects.values('status').annotate(n=Count('id'))}
    return {'new': counts.get('new', 0), 'progress': counts.get('progress', 0), 'all': sum(counts.values())}


@register.simple_tag
def admin_menu():
    return [{'label': m._meta.verbose_name_plural, 'url': _changelist(m)} for m in CONTENT]


@register.simple_tag
def admin_dashboard():
    return {
        'recent': Lead.objects.all()[:6],
        'content': [{'label': m._meta.verbose_name_plural, 'url': _changelist(m), 'count': m.objects.count()}
                    for m in CONTENT],
    }

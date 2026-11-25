from django import template
from django.db.models import Count

from ..models import Lead

register = template.Library()


@register.simple_tag
def admin_stats():
    counts = {r['status']: r['n'] for r in Lead.objects.values('status').annotate(n=Count('id'))}
    return {'new': counts.get('new', 0), 'progress': counts.get('progress', 0), 'all': sum(counts.values())}

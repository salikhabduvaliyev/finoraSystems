import re

from django import template
from django.template.loader import render_to_string
from django.utils.html import conditional_escape, escape, format_html
from django.utils.safestring import mark_safe

from ..media import parse_video
from ..models import lines as _lines

register = template.Library()


@register.filter
def lines(value):
    """Matnni qatorlarga ajratadi: har bir bo'sh bo'lmagan qator — alohida punkt."""
    return _lines(value)


@register.filter
def accent(value):
    """'Matn *urg'u* bilan' -> urg'u qismi <span> ichida."""
    return mark_safe(re.sub(r'\*(.+?)\*', r'<span>\1</span>', str(conditional_escape(value or ''))))


@register.filter
def paras(value):
    """Bo'sh qator bilan ajratilgan matn -> <p> xatboshilar."""
    blocks = [b.strip() for b in re.split(r'\n\s*\n', str(value or '').replace('\r', '')) if b.strip()]
    return mark_safe(''.join('<p>' + escape(b).replace(chr(10), '<br>') + '</p>' for b in blocks))


@register.filter
def pad2(value):
    return f'{int(value):02d}'


@register.filter
def tel(value):
    return 'tel:' + re.sub(r'[^\d+]', '', str(value or ''))


@register.simple_tag
def svg(name):
    """templates/svg/ ichidagi tayyor SVG'ni joylaydi (dizayndagi illyustratsiyalar)."""
    return mark_safe(render_to_string(f'svg/{name}.svg'))


@register.simple_tag
def fig(obj):
    """Kartochka rasmi: yuklangan rasm bo'lsa — rasm, aks holda soha illyustratsiyasi."""
    if getattr(obj, 'image', None):
        return format_html("<div class='fig'><img src='{}' alt='{}' loading='lazy'></div>", obj.image.url,
                           getattr(obj, 'title', ''))
    return mark_safe(f"<div class='fig'>{render_to_string('svg/mock/' + (obj.mock or 'savdo') + '.svg')}</div>")


@register.simple_tag
def video(src, title=''):
    """YouTube/Vimeo — bosilganda yuklanadigan pleyer; fayl — <video>."""
    v = parse_video(src)
    if not v:
        return ''
    if v['kind'] == 'file':
        return format_html("<div class='vid'><video src='{}' controls preload='metadata' playsinline></video></div>", v['src'])
    if v['kind'] == 'youtube':
        embed = f"https://www.youtube-nocookie.com/embed/{v['id']}?autoplay=1&rel=0"
        thumb = format_html("<img src='https://i.ytimg.com/vi/{}/hqdefault.jpg' alt='' loading='lazy'>", v['id'])
    else:
        embed = f"https://player.vimeo.com/video/{v['id']}?autoplay=1"
        thumb = ''
    return format_html(
        "<div class='vid{}'><button type='button' class='vplay' data-embed='{}' data-title='{}' "
        "aria-label='Videoni ko‘rish: {}'>{}<span class='pl' aria-hidden='true'></span></button></div>",
        ' vv' if v.get('vertical') else '', embed, title, title, thumb)

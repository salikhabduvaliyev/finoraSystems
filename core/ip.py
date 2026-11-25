"""Mijozning haqiqiy IP manzili.

PythonAnywhere (va nginx) proksi orqasida REMOTE_ADDR har doim proksining manzili bo'ladi,
haqiqiy IP esa proksi qo'yadigan X-Real-IP sarlavhasida keladi. Shu funksiya ham ariza
limitida (views.py), ham admin kirish himoyasida (django-axes) ishlatiladi.
"""


def client_ip(request):
    meta = request.META
    return (meta.get('HTTP_X_REAL_IP') or meta.get('REMOTE_ADDR') or '').strip()

"""Yangi ariza haqida Telegramga xabar (bir yoki bir nechta chat ID ga)."""
import json
import logging
import re
import urllib.request
from html import escape

from django.utils import timezone

from .models import SiteSettings

log = logging.getLogger('core')


def notify_lead(lead):
    s = SiteSettings.load()
    token = (s.tg_bot_token or '').strip()
    chats = [c for c in re.split(r'[\s,;]+', s.tg_chat_id or '') if c]
    if not token or not chats:
        return

    digits = re.sub(r'\D', '', lead.phone or '')
    text = '\n'.join(x for x in [
        '🔔 <b>Yangi ariza — Finora Systems</b>\n',
        f'👤 <b>Ism:</b> {escape(lead.name)}',
        f'📞 <b>Telefon:</b> <code>{escape(lead.phone)}</code>',
        lead.service and f'🧩 <b>Xizmat:</b> {escape(lead.service)}',
        lead.message and f'💬 <b>Xabar:</b> <i>{escape(lead.message)}</i>',
        f'📍 <b>Manba:</b> {escape(lead.source_label)}',
        lead.page and f'🔗 <b>Sahifa:</b> {escape(lead.page)}',
        f"⏰ <b>Vaqt:</b> {timezone.localtime().strftime('%d.%m.%Y %H:%M')}",
    ] if x)
    payload = {'text': text, 'parse_mode': 'HTML', 'disable_web_page_preview': True}
    if digits:
        payload['reply_markup'] = {'inline_keyboard': [[{'text': '💬 Telegramdan yozish', 'url': f'https://t.me/+{digits}'}]]}

    url = f'https://api.telegram.org/bot{token}/sendMessage'
    for chat in chats:
        body = json.dumps({**payload, 'chat_id': chat}).encode()
        req = urllib.request.Request(url, data=body, headers={'Content-Type': 'application/json'})
        try:
            # urllib PythonAnywhere proksisini (HTTPS_PROXY) avtomatik ishlatadi
            urllib.request.urlopen(req, timeout=8).read()
        except Exception as e:  # tarmoq xatosi arizani saqlashga xalaqit bermasin
            log.warning('Telegram (%s) ga yuborilmadi: %s', chat, e)

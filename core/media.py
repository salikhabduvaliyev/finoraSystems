"""Video havolalarini aniqlash va URL uchun slug yasash."""
import re
import unicodedata

_VIDEO_FILE = re.compile(r'^(/media/\S+|https?://\S+)\.(mp4|webm|mov)(\?\S*)?$', re.I)
_YOUTUBE = re.compile(
    r'^(?:https?://)?(?:www\.|m\.)?(?:youtube\.com/(?:watch\?(?:.*&)?v=|embed/|shorts/|live/)|youtu\.be/)([\w-]{11})', re.I)
_INSTAGRAM = re.compile(r'^(?:https?://)?(?:www\.)?instagram\.com/(?:[\w.]+/)?(reel|reels|p|tv)/([\w-]+)', re.I)
_VIMEO = re.compile(r'^(?:https?://)?(?:www\.|player\.)?vimeo\.com/(?:video/)?(\d+)', re.I)


def parse_video(url):
    url = str(url or '').strip()
    if not url:
        return None
    if _VIDEO_FILE.match(url):
        return {'kind': 'file', 'src': url}
    m = _YOUTUBE.match(url)
    if m:
        return {'kind': 'youtube', 'id': m.group(1), 'vertical': '/shorts/' in url.lower()}
    m = _INSTAGRAM.match(url)
    if m:
        kind = 'p' if m.group(1).lower() == 'p' else 'reel'
        return {'kind': 'instagram', 'id': m.group(2), 'embed': f'https://www.instagram.com/{kind}/{m.group(2)}/embed/',
                'vertical': True}
    m = _VIMEO.match(url)
    if m:
        return {'kind': 'vimeo', 'id': m.group(1)}
    return None


_CYR = dict(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюяўқғҳ',
                ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'j', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
                 'u', 'f', 'x', 'ts', 'ch', 'sh', 'sh', '', 'i', '', 'e', 'yu', 'ya', 'o', 'q', 'g', 'h']))


def slugify_uz(text):
    s = ''.join(_CYR.get(c, c) for c in str(text or '').lower())
    s = re.sub(r"[ʻʼ'‘’`]", '', s)
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:60] or 'x'

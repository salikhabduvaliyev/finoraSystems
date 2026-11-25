# Finora Systems — sayt va admin panel

Django 5.2 LTS + SQLite. Kutubxonalar: `Django`, `Pillow`, `django-axes`.

## Kompyuterda ishga tushirish

```bash
pip install -r requirements.txt
echo DJANGO_DEBUG=1 > .env
python manage.py migrate
python manage.py loaddata initial_content   # sayt kontenti (faqat birinchi marta)
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8765
```

Sayt: http://127.0.0.1:8765 · Admin: http://127.0.0.1:8765/admin/

---

## PythonAnywhere'ga joylash — tez yo'l (bitta buyruq)

1. PythonAnywhere → **Account → API Token → Create a new API token** (bir marta).
2. **Consoles → Bash** ni oching va yozing:

```bash
git clone https://github.com/salikhabduvaliyev/finoraSystems.git ~/finora && bash ~/finora/deploy/pythonanywhere.sh
```

Skript hammasini o'zi qiladi: virtual muhit, kutubxonalar, `.env`, baza va kontent, statik fayllar,
web ilova, WSGI, static/media yo'llari, Reload. Faqat admin login va parolni so'raydi.

**Yangilash:** `bash ~/finora/deploy/pythonanywhere.sh` (git pull'ni ham o'zi qiladi).

---

## PythonAnywhere'ga joylash — qo'lda (har bir qadam)

`USERNAME` o'rniga PythonAnywhere login'ingizni yozing. Barcha buyruqlar **Consoles → Bash** da bajariladi.

### 1. Loyihani yuklab olish

```bash
git clone https://github.com/salikhabduvaliyev/finoraSystems.git ~/finora
```

### 2. Virtual muhit va kutubxonalar

```bash
mkvirtualenv --python=/usr/bin/python3.12 finora-venv
pip install -r ~/finora/requirements.txt
```

`python3.12` bo'lmasa, borini tanlang: `ls /usr/bin/python3.*`

### 3. Maxfiy sozlamalar (`.env`)

```bash
cd ~/finora
python -c "import secrets;print('DJANGO_SECRET_KEY='+secrets.token_urlsafe(50))" > .env
echo "DJANGO_DEBUG=0" >> .env
echo "DJANGO_ALLOWED_HOSTS=USERNAME.pythonanywhere.com" >> .env
```

`.env` GitHub'ga yuklanmaydi va yuklanmasligi kerak.

### 4. Baza, kontent, admin

```bash
python manage.py migrate
python manage.py loaddata initial_content   # xizmatlar, keyslar, jamoa, sozlamalar
python manage.py createsuperuser            # admin login va parol
python manage.py collectstatic --noinput
```

`loaddata` ni **faqat birinchi marta** ishga tushiring, chunki keyinchalik admin'da qilingan o'zgarishlarni boshlang'ich holatga qaytaradi.

### 5. Web ilova

*Web → Add a new web app → Manual configuration* — Python versiyasi 2-qadamdagi bilan bir xil bo'lsin.

- **Source code:** `/home/USERNAME/finora`
- **Virtualenv:** `/home/USERNAME/.virtualenvs/finora-venv`
- **WSGI configuration file** — ichidagi hamma narsani shunga almashtiring:

```python
import os, sys
path = '/home/USERNAME/finora'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'finora.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

- **Static files:**

| URL | Directory |
|---|---|
| `/static/` | `/home/USERNAME/finora/staticfiles` |
| `/media/` | `/home/USERNAME/finora/media` |

- **Force HTTPS** ni yoqing → yashil **Reload** tugmasini bosing.

### 6. Telegram bildirishnoma

Bot token va chat ID'lar xavfsizlik uchun GitHub'ga yuklanmagan. Admin → **Sayt sozlamalari** → *Telegram bildirishnoma* bo'limiga qayta kiriting.

### 7. Tekshirish

`https://USERNAME.pythonanywhere.com` va `/admin/`. Xato bo'lsa — *Web* bo'limidagi **Error log**.

---

## Yangilash (kod o'zgarganda)

Kompyuterda: `git add . && git commit -m "..." && git push`. Keyin PythonAnywhere Bash'da:

```bash
cd ~/finora && workon finora-venv
git pull
pip install -r requirements.txt        # kutubxonalar o'zgargan bo'lsa
python manage.py migrate               # modellar o'zgargan bo'lsa
python manage.py collectstatic --noinput
```

So'ng *Web* bo'limida **Reload**.

Admin orqali yuklangan rasm va videolar serverdagi `media/` papkasida qoladi, `git pull` ularga tegmaydi.

## Admin kirish himoyasi (django-axes)

Parol **5 marta** noto'g'ri kiritilsa, shu IP'dan kirish **1 soatga** bloklanadi. Urinishlar admin'da *Axes → Access attempts* bo'limida ko'rinadi.

```bash
python manage.py axes_reset              # bloklarni olib tashlash
python manage.py changepassword admin    # parolni unutgan bo'lsangiz
```

## Bepul tarif haqida

- 3 oyda bir marta *Web* bo'limida **"Run until 3 months from today"** ni bosing, aks holda sayt to'xtaydi.
- Disk cheklangan: katta videolarni YouTube'ga joylab, havolasini qo'ying.
- O'z domeningiz (masalan, finora.uz) uchun pullik tarif kerak.

## Zaxira nusxa

Serverdagi `db.sqlite3` va `media/` ni vaqti-vaqti bilan yuklab oling (*Files* bo'limi) — arizalar va admin o'zgarishlari faqat shu yerda.

## Tuzilma

```
finora/                 Django sozlamalari, URL'lar
core/models.py          bo'limlar: Xizmatlar, Sohalar, Keyslar, Jamoa, Arizalar, Sozlamalar …
core/admin.py           admin panel
core/views.py           sahifalar va ariza qabul qilish (/api/lead)
core/notify.py          Telegram bildirishnoma
core/fixtures/          boshlang'ich kontent (initial_content.json)
core/templates/         sayt va admin shablonlari, SVG illyustratsiyalar
static/                 CSS, JS, logo
media/                  rasm va videolar
```

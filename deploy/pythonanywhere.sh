#!/bin/bash
# Finora Systems — PythonAnywhere'ga bitta buyruq bilan joylash va yangilash.
#
# Birinchi marta (PythonAnywhere → Consoles → Bash):
#   git clone https://github.com/salikhabduvaliyev/finoraSystems.git ~/finora && bash ~/finora/deploy/pythonanywhere.sh
#
# Keyingi yangilashlar uchun:
#   bash ~/finora/deploy/pythonanywhere.sh
#
# Skript qayta ishga tushirilsa ham xavfsiz: bor narsani qayta yaratmaydi, kontentni ustidan yozmaydi.
set -euo pipefail

APP_DIR="$HOME/finora"
VENV="$HOME/.virtualenvs/finora-venv"
DOMAIN="$(echo "$USER" | tr '[:upper:]' '[:lower:]').pythonanywhere.com"
API="https://www.pythonanywhere.com/api/v0/user/$USER"

step() { echo; echo "==> $*"; }

cd "$APP_DIR"

step "Kodni yangilash (git pull)"
git pull --ff-only || echo "   (git pull o'tkazib yuborildi)"

step "Python versiyasini tanlash"
PYBIN=""
for v in 3.13 3.12 3.11 3.10; do
  if [ -x "/usr/bin/python$v" ]; then PYBIN="/usr/bin/python$v"; PYVER="$v"; break; fi
done
[ -n "$PYBIN" ] || { echo "Python 3.10+ topilmadi"; exit 1; }
echo "   $PYBIN"

step "Virtual muhit va kutubxonalar"
[ -d "$VENV" ] || "$PYBIN" -m venv "$VENV"
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -r requirements.txt
PY="$VENV/bin/python"

step "Maxfiy sozlamalar (.env)"
if [ ! -f .env ]; then
  {
    echo "DJANGO_SECRET_KEY=$("$PY" -c 'import secrets;print(secrets.token_urlsafe(50))')"
    echo "DJANGO_DEBUG=0"
    echo "DJANGO_ALLOWED_HOSTS=$DOMAIN"
  } > .env
  chmod 600 .env
  echo "   yaratildi"
else
  echo "   bor, o'zgartirilmadi"
fi

step "Baza"
"$PY" manage.py migrate --noinput
if [ "$("$PY" manage.py shell -c 'from core.models import Service; print(Service.objects.exists())' 2>/dev/null | tail -1)" != "True" ]; then
  echo "   bo'sh baza — boshlang'ich kontent yuklanmoqda"
  "$PY" manage.py loaddata initial_content
fi

step "Statik fayllar"
"$PY" manage.py collectstatic --noinput -v 0

if [ "$("$PY" manage.py shell -c 'from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).exists())' 2>/dev/null | tail -1)" != "True" ]; then
  step "Admin foydalanuvchi yaratish (login va parolni o'zingiz kiriting)"
  "$PY" manage.py createsuperuser
fi

step "Web ilova sozlamalari"
if [ -z "${API_TOKEN:-}" ]; then
  cat <<EOF
   API token topilmadi. Uni bir marta yarating:
     Account → "API Token" bo'limi → "Create a new API token"
   So'ng YANGI Bash konsol ochib, skriptni qayta ishga tushiring:
     bash ~/finora/deploy/pythonanywhere.sh
EOF
  exit 1
fi
AUTH="Authorization: Token $API_TOKEN"

# Eslatma: yo'q ilova uchun API 404 emas, 403 qaytaradi — shuning uchun ro'yxatdan tekshiramiz
if ! curl -sf -H "$AUTH" "$API/webapps/" | grep -q "\"domain_name\": *\"$DOMAIN\""; then
  curl -sf -H "$AUTH" -X POST "$API/webapps/" \
    -d "domain_name=$DOMAIN" -d "python_version=python${PYVER/./}" > /dev/null
  echo "   web ilova yaratildi: $DOMAIN"
fi
curl -sf -H "$AUTH" -X PATCH "$API/webapps/$DOMAIN/" \
  -d "virtualenv_path=$VENV" -d "source_directory=$APP_DIR" -d "force_https=true" > /dev/null

WSGI="/var/www/${DOMAIN//./_}_wsgi.py"
cat > "$WSGI" <<EOF
import os, sys
path = '$APP_DIR'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'finora.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
EOF
echo "   WSGI: $WSGI"

EXISTING="$(curl -sf -H "$AUTH" "$API/webapps/$DOMAIN/static_files/")"
for pair in "/static/|$APP_DIR/staticfiles" "/media/|$APP_DIR/media"; do
  url="${pair%%|*}"; dir="${pair##*|}"
  if ! echo "$EXISTING" | grep -q "\"url\": *\"$url\""; then
    curl -sf -H "$AUTH" -X POST "$API/webapps/$DOMAIN/static_files/" -d "url=$url" -d "path=$dir" > /dev/null
    echo "   static: $url -> $dir"
  fi
done

step "Qayta ishga tushirish (Reload)"
curl -sf -H "$AUTH" -X POST "$API/webapps/$DOMAIN/reload/" > /dev/null

echo
echo "Tayyor!  Sayt:  https://$DOMAIN"
echo "         Admin: https://$DOMAIN/admin/"
echo "Telegram bildirishnoma uchun: Admin → Sayt sozlamalari → bot token va chat ID'larni kiriting."

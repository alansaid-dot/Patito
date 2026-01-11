#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset

echo "=== INSTALANDO DEPENDENCIAS ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== VERIFICANDO VARIABLES DE ENTORNO ==="
echo "DJANGO_SETTINGS_MODULE: ${DJANGO_SETTINGS_MODULE:-No configurado}"
echo "DATABASE_URL: ${DATABASE_URL:-NO CONFIGURADA - ESTE ES EL PROBLEMA}"

echo "=== RECOLECTANDO STATIC FILES ==="
python manage.py collectstatic --noinput --clear

echo "=== EJECUTANDO MIGRACIONES ==="
# Solo intenta migrar si DATABASE_URL está configurada
if [[ -n "${DATABASE_URL:-}" ]]; then
    python manage.py migrate --noinput
else
    echo "ADVERTENCIA: DATABASE_URL no configurada. Saltando migraciones."
    echo "Asegúrate de añadir DATABASE_URL en Render Environment."
fi

echo "=== BUILD COMPLETADO ==="
#!/bin/sh
set -e

echo "Esperando a la base de datos..."
python manage.py migrate --noinput

echo "Compilando traducciones..."
python manage.py compilemessages || true

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@veripay.com', 'admin123')
    print('Superusuario creado: admin / admin123')
if not User.objects.filter(username='usuario').exists():
    User.objects.create_user('usuario', 'usuario@veripay.com', 'usuario123', is_staff=False)
    print('Usuario final creado: usuario / usuario123')
"

if [ "${RUN_SEED:-true}" = "true" ]; then
    echo "Cargando datos ficticios..."
    python manage.py seed_data || true
fi

echo "Iniciando servidor en puerto ${PORT:-8000}..."
exec gunicorn veripay_project.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2 --timeout 120

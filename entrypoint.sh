#!/bin/sh
set -e

echo "Esperando a la base de datos..."
python manage.py migrate --noinput

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput

# Crear superusuario si no existe
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@veripay.com', 'admin123')
    print('Superusuario creado: admin / admin123')
else:
    print('Superusuario ya existe')
"

echo "Iniciando servidor..."
exec gunicorn veripay_project.wsgi:application --bind 0.0.0.0:8000

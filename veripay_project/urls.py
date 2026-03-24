# Autor: Equipo VeriPay
# Configuración de URLs principal
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Core: dashboard, login, logout, reportes, email
    path('', include('core.urls')),
    # Apps
    path('proveedores/', include('proveedores.urls')),
    path('facturas/', include('facturas.urls')),
    path('pagos/', include('pagos.urls')),
    path('certificados/', include('certificados.urls')),
    path('conciliacion/', include('conciliacion.urls')),
    # Panel admin personalizado
    path('admin-panel/', include('core.admin_panel.urls')),
    # Django admin (mantener para compatibilidad)
    path('django-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

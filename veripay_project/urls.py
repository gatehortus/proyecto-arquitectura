# Autor: Equipo VeriPay
# Configuración de URLs principal
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from proveedores.urls import api_urlpatterns as proveedores_api_urlpatterns

urlpatterns = [
    # Core: dashboard, login, logout, reportes, email
    path('', include('core.urls')),
    # Apps
    path('proveedores/', include('proveedores.urls')),
    path('api/', include(proveedores_api_urlpatterns)),
    path('facturas/', include('facturas.urls')),
    path('pagos/', include('pagos.urls')),
    path('certificados/', include('certificados.urls')),
    path('conciliacion/', include('conciliacion.urls')),
    path('reportes/', include('reportes.urls')),
    # Panel admin personalizado
    path('admin-panel/', include('core.admin_panel.urls')),
    # Django admin (mantener para compatibilidad)
    path('django-admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

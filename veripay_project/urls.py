from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from proveedores.urls import api_urlpatterns as proveedores_api_urlpatterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/', include(proveedores_api_urlpatterns)),
    path('django-admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('core.urls')),
    path('proveedores/', include('proveedores.urls')),
    path('facturas/', include('facturas.urls')),
    path('pagos/', include('pagos.urls')),
    path('certificados/', include('certificados.urls')),
    path('conciliacion/', include('conciliacion.urls')),
    path('reportes/', include('reportes.urls')),
    path('admin-panel/', include('core.admin_panel.urls')),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

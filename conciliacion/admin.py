from django.contrib import admin

from .models import Coincidencia, ProcesoReconciliacion
from .services import ejecutar_conciliacion


@admin.action(description="Ejecutar conciliaci\u00f3n con pagos")
def ejecutar_conciliacion_basica(modeladmin, request, queryset):
    for proceso in queryset:
        ejecutar_conciliacion(proceso)


@admin.register(ProcesoReconciliacion)
class ProcesoReconciliacionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'estado',
        'tolerancia',
        'total_facturas',
        'facturas_conciliadas',
        'facturas_pendientes',
        'created_at',
    )
    list_filter = ('estado', 'created_at')
    search_fields = ('id',)
    actions = [ejecutar_conciliacion_basica]


@admin.register(Coincidencia)
class CoincidenciaAdmin(admin.ModelAdmin):
    list_display = (
        'factura',
        'proceso',
        'tipo',
        'porcentaje_confianza',
        'created_at',
    )
    list_filter = ('tipo', 'created_at')
    search_fields = (
        'factura__numero_factura',
    )

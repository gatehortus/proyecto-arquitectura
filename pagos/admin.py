from django.contrib import admin
from .models import ArchivoPagos, RegistroPago


@admin.register(ArchivoPagos)
class ArchivoPagosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'formato',
        'total_registros',
        'registros_procesados',
        'procesado',
        'created_at',
    )
    list_filter = ('procesado', 'formato', 'created_at')
    search_fields = ('id',)


@admin.register(RegistroPago)
class RegistroPagoAdmin(admin.ModelAdmin):
    list_display = (
        'referencia',
        'archivo',
        'monto',
        'fecha',
        'concepto',
        'numero_linea',
    )
    list_filter = ('fecha',)
    search_fields = ('referencia', 'concepto')
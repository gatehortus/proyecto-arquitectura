from django.contrib import admin
from .models import Factura


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = (
        'numero_factura',
        'proveedor',
        'monto_total',
        'monto_pagado',
        'estado',
        'fecha_emision',
        'fecha_vencimiento',
    )
    list_filter = ('estado', 'fecha_emision', 'fecha_vencimiento')
    search_fields = ('numero_factura', 'uuid_fiscal', 'proveedor__nombre')
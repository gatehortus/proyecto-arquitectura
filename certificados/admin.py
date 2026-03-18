from django.contrib import admin
from .models import CertificadoBancario


@admin.register(CertificadoBancario)
class CertificadoBancarioAdmin(admin.ModelAdmin):
    list_display = (
        'numero_certificado',
        'banco',
        'cuenta_origen',
        'monto_pagado',
        'fecha_pago',
        'autenticidad_verificada',
    )
    list_filter = ('autenticidad_verificada', 'banco', 'fecha_pago')
    search_fields = ('numero_certificado', 'referencia', 'banco')
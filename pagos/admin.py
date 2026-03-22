from django.contrib import admin
from .models import ArchivoPagos, RegistroPago
import csv


@admin.action(description="Procesar archivo de pagos")
def procesar_archivo_pagos(modeladmin, request, queryset):
    for archivo_pago in queryset:

        if not archivo_pago.archivo:
            continue

        ruta = archivo_pago.archivo.path

        with open(ruta, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            contador = 0

            for fila in reader:
                RegistroPago.objects.create(
                    archivo=archivo_pago,
                    referencia=fila.get("referencia"),
                    monto=fila.get("monto"),
                    fecha=fila.get("fecha"),
                    concepto=fila.get("concepto"),
                    numero_linea=contador
                )
                contador += 1

        archivo_pago.total_registros = contador
        archivo_pago.registros_procesados = contador
        archivo_pago.procesado = True
        archivo_pago.save()


@admin.register(ArchivoPagos)
class ArchivoPagosAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "archivo",
        "formato",
        "total_registros",
        "procesado",
    )
    actions = [procesar_archivo_pagos]


@admin.register(RegistroPago)
class RegistroPagoAdmin(admin.ModelAdmin):
    list_display = (
        "referencia",
        "archivo",
        "monto",
        "fecha",
        "concepto",
        "numero_linea",
    )
    
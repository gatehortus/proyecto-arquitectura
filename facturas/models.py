from django.db import models
import uuid
from proveedores.models import Proveedor


class Factura(models.Model):

    class EstadoFactura(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        PAGADA = 'PAGADA', 'Pagada'
        PARCIAL = 'PARCIAL', 'Parcial'
        RECHAZADA = 'RECHAZADA', 'Rechazada'
        NO_ENCONTRADA = 'NO_ENCONTRADA', 'No encontrada'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.CASCADE,
        related_name='facturas'
    )

    numero_factura = models.CharField(
        max_length=100,
        unique=True
    )

    uuid_fiscal = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    monto_total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    monto_pagado = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    fecha_emision = models.DateField()

    fecha_vencimiento = models.DateField(
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=20,
        choices=EstadoFactura.choices,
        default=EstadoFactura.PENDIENTE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.numero_factura} - {self.proveedor.nombre}"
# creamos una factura que pertenece a un proveedor, tiene número, monto total y pagado, fechas y estado, conectada con Proveedor


from django.db import models
import uuid


class CertificadoBancario(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    numero_certificado = models.CharField(
        max_length=100,
        unique=True
    )

    banco = models.CharField(
        max_length=100
    )

    cuenta_origen = models.CharField(
        max_length=100
    )

    monto_pagado = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    fecha_pago = models.DateField()

    referencia = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    autenticidad_verificada = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.numero_certificado} - {self.banco}"
# Create your models here.

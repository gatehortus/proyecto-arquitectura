from django.db import models
import uuid


class ArchivoPagos(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    archivo = models.FileField(
        upload_to="pagos/"
    )

    formato = models.CharField(
        max_length=20
    )

    total_registros = models.IntegerField(
        default=0
    )

    registros_procesados = models.IntegerField(
        default=0
    )

    procesado = models.BooleanField(
        default=False
    )

    procesado_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Archivo {self.id}"

class RegistroPago(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    archivo = models.ForeignKey(
        ArchivoPagos,
        on_delete=models.CASCADE,
        related_name="registros"
    )

    referencia = models.CharField(
        max_length=100
    )

    monto = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    fecha = models.DateField()

    concepto = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    numero_linea = models.IntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.referencia} - {self.monto}"
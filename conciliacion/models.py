from django.db import models
import uuid
from facturas.models import Factura
from pagos.models import RegistroPago
from certificados.models import CertificadoBancario


class ProcesoReconciliacion(models.Model):

    class EstadoProceso(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        EN_PROCESO = 'EN_PROCESO', 'En proceso'
        FINALIZADO = 'FINALIZADO', 'Finalizado'
        ERROR = 'ERROR', 'Error'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    estado = models.CharField(
        max_length=20,
        choices=EstadoProceso.choices,
        default=EstadoProceso.PENDIENTE
    )

    tolerancia = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_facturas = models.IntegerField(
        default=0
    )

    facturas_conciliadas = models.IntegerField(
        default=0
    )

    facturas_pendientes = models.IntegerField(
        default=0
    )

    iniciado_at = models.DateTimeField(
        blank=True,
        null=True
    )

    finalizado_at = models.DateTimeField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Proceso {self.id} - {self.estado}"


class Coincidencia(models.Model):

    class TipoCoincidencia(models.TextChoices):
        EXACTA = 'EXACTA', 'Exacta'
        PARCIAL = 'PARCIAL', 'Parcial'
        INCONSISTENTE = 'INCONSISTENTE', 'Inconsistente'
        NO_ENCONTRADA = 'NO_ENCONTRADA', 'No encontrada'

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    proceso = models.ForeignKey(
        ProcesoReconciliacion,
        on_delete=models.CASCADE,
        related_name='coincidencias'
    )

    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        related_name='coincidencias'
    )

    registro_pago = models.ForeignKey(
        RegistroPago,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='coincidencias'
    )

    certificado_bancario = models.ForeignKey(
        CertificadoBancario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='coincidencias'
    )

    tipo = models.CharField(
        max_length=20,
        choices=TipoCoincidencia.choices,
        default=TipoCoincidencia.NO_ENCONTRADA
    )

    porcentaje_confianza = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    observacion = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.factura.numero_factura} - {self.tipo}"
       
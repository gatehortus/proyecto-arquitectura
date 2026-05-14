# Autor: Equipo VeriPay
# Motor de conciliación automática con porcentaje de confianza
from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from django.utils.translation import gettext as _
from facturas.models import Factura
from pagos.models import RegistroPago
from certificados.models import CertificadoBancario
from .models import ProcesoReconciliacion, Coincidencia


@transaction.atomic
def ejecutar_conciliacion(proceso):
    facturas = Factura.objects.all()

    proceso.total_facturas = facturas.count()
    proceso.facturas_conciliadas = 0
    proceso.facturas_pendientes = 0

    for factura in facturas:
        pago = RegistroPago.objects.filter(
            referencia__iexact=factura.numero_factura
        ).first()

        if pago and pago.monto >= factura.monto_total:
            factura.estado = Factura.EstadoFactura.PAGADA
            tipo = Coincidencia.TipoCoincidencia.EXACTA
            proceso.facturas_conciliadas += 1
        elif pago:
            factura.estado = Factura.EstadoFactura.PARCIAL
            tipo = Coincidencia.TipoCoincidencia.PARCIAL
            proceso.facturas_pendientes += 1
        else:
            factura.estado = Factura.EstadoFactura.NO_ENCONTRADA
            tipo = Coincidencia.TipoCoincidencia.NO_ENCONTRADA
            proceso.facturas_pendientes += 1

        factura.save()

        Coincidencia.objects.create(
            proceso=proceso,
            factura=factura,
            registro_pago=pago,
            tipo=tipo,
            porcentaje_confianza=100,
            observacion=_("Conciliación usando archivo de pagos"),
        )

    proceso.estado = ProcesoReconciliacion.EstadoProceso.FINALIZADO
    proceso.save()

    return proceso


def run_reconciliation(tolerancia=5):
    """
    Ejecuta el proceso de conciliación automática.
    1. Busca coincidencia exacta por referencia en pagos
    2. Busca coincidencia por monto con tolerancia
    3. Busca certificado bancario asociado
    4. Calcula porcentaje de confianza
    5. Clasifica: EXACTA (>=90%), PARCIAL (50-89%), INCONSISTENTE (20-49%), NO_ENCONTRADA (<20%)
    """
    facturas = Factura.objects.filter(estado__in=['PENDIENTE', 'PARCIAL', 'NO_ENCONTRADA'])
    registros = RegistroPago.objects.all()
    certificados = CertificadoBancario.objects.all()

    proceso = ProcesoReconciliacion.objects.create(
        estado='EN_PROCESO',
        tolerancia=Decimal(str(tolerancia)),
        total_facturas=facturas.count(),
        facturas_conciliadas=0,
        facturas_pendientes=facturas.count(),
        iniciado_at=timezone.now(),
    )

    conciliadas = 0

    for factura in facturas:
        confianza = Decimal('0')
        registro_match = None
        certificado_match = None
        observaciones = []

        # 1. Buscar pago por referencia exacta (número de factura)
        pago_exacto = registros.filter(referencia__icontains=factura.numero_factura).first()
        if pago_exacto:
            registro_match = pago_exacto
            confianza += Decimal('40')
            observaciones.append(_("Referencia encontrada en pagos"))

            # Verificar monto
            diff_pago = abs(factura.monto_total - pago_exacto.monto)
            tolerancia_monto = factura.monto_total * Decimal(str(tolerancia)) / Decimal('100')
            if diff_pago <= tolerancia_monto:
                confianza += Decimal('30')
                observaciones.append(_("Monto dentro de tolerancia"))
            elif pago_exacto.monto < factura.monto_total:
                confianza += Decimal('15')
                observaciones.append(
                    _("Pago parcial: $%(monto)s") % {"monto": pago_exacto.monto}
                )
        else:
            # 2. Buscar por monto similar
            for registro in registros:
                diff = abs(factura.monto_total - registro.monto)
                tolerancia_monto = factura.monto_total * Decimal(str(tolerancia)) / Decimal('100')
                if diff <= tolerancia_monto:
                    registro_match = registro
                    confianza += Decimal('25')
                    observaciones.append(
                        _("Monto similar encontrado: $%(monto)s") % {"monto": registro.monto}
                    )
                    break

        # 3. Buscar certificado bancario
        cert_match = certificados.filter(referencia__icontains=factura.numero_factura).first()
        if not cert_match:
            cert_match = certificados.filter(monto_pagado=factura.monto_total).first()

        if cert_match:
            certificado_match = cert_match
            confianza += Decimal('20')
            observaciones.append(
                _("Certificado: %(numero)s") % {
                    "numero": cert_match.numero_certificado
                }
            )
            if cert_match.autenticidad_verificada:
                confianza += Decimal('10')
                observaciones.append(_("Certificado verificado"))

        # 4. Clasificar
        confianza = min(confianza, Decimal('100'))
        if confianza >= 90:
            tipo = 'EXACTA'
        elif confianza >= 50:
            tipo = 'PARCIAL'
        elif confianza >= 20:
            tipo = 'INCONSISTENTE'
        else:
            tipo = 'NO_ENCONTRADA'

        Coincidencia.objects.create(
            proceso=proceso,
            factura=factura,
            registro_pago=registro_match,
            certificado_bancario=certificado_match,
            tipo=tipo,
            porcentaje_confianza=confianza,
            observacion='; '.join(observaciones) if observaciones else _("Sin coincidencias encontradas"),
        )

        # Actualizar estado de factura
        if tipo == 'EXACTA':
            factura.estado = 'PAGADA'
            if registro_match:
                factura.monto_pagado = registro_match.monto
            conciliadas += 1
        elif tipo == 'PARCIAL':
            factura.estado = 'PARCIAL'
            if registro_match:
                factura.monto_pagado = registro_match.monto
            conciliadas += 1
        elif tipo == 'INCONSISTENTE':
            factura.estado = 'RECHAZADA'
        else:
            factura.estado = 'NO_ENCONTRADA'
        factura.save()

    proceso.estado = 'FINALIZADO'
    proceso.facturas_conciliadas = conciliadas
    proceso.facturas_pendientes = proceso.total_facturas - conciliadas
    proceso.finalizado_at = timezone.now()
    proceso.save()

    return proceso

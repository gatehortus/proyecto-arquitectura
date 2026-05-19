from django.test import TestCase

from conciliacion.models import Coincidencia, ProcesoReconciliacion
from conciliacion.services import ejecutar_conciliacion
from facturas.models import Factura
from pagos.models import ArchivoPagos, RegistroPago
from proveedores.models import Proveedor


class MotorDeConciliacionTests(TestCase):
    def test_factura_con_pago_exacto_queda_pagada(self):
        proveedor = Proveedor.objects.create(
            nombre='Acme', nit='900-1', email='acme@example.com'
        )
        archivo = ArchivoPagos.objects.create(archivo='pagos/test.csv', formato='csv')
        factura = Factura.objects.create(
            proveedor=proveedor,
            numero_factura='FAC-001',
            monto_total=100,
            fecha_emision='2026-01-01',
        )
        RegistroPago.objects.create(
            archivo=archivo, referencia='FAC-001', monto=100, fecha='2026-01-02'
        )
        proceso = ProcesoReconciliacion.objects.create()

        ejecutar_conciliacion(proceso)

        factura.refresh_from_db()
        coincidencia = Coincidencia.objects.get(proceso=proceso, factura=factura)
        self.assertEqual(factura.estado, Factura.EstadoFactura.PAGADA)
        self.assertEqual(coincidencia.tipo, Coincidencia.TipoCoincidencia.EXACTA)

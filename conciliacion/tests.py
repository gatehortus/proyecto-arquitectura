from django.test import TestCase

from conciliacion.models import Coincidencia, ProcesoReconciliacion
from conciliacion.services import ejecutar_conciliacion
from facturas.models import Factura
from pagos.models import ArchivoPagos, RegistroPago
from proveedores.models import Proveedor


class EjecutarConciliacionTests(TestCase):
    def setUp(self):
        self.proveedor = Proveedor.objects.create(
            nombre='Proveedor Test',
            nit='123456789',
            email='proveedor@test.com',
        )
        self.archivo_pagos = ArchivoPagos.objects.create(
            archivo='pagos/test.csv',
            formato='csv',
        )

    def crear_factura(self, numero_factura, monto_total):
        return Factura.objects.create(
            proveedor=self.proveedor,
            numero_factura=numero_factura,
            monto_total=monto_total,
            fecha_emision='2026-01-01',
        )

    def crear_pago(self, referencia, monto):
        return RegistroPago.objects.create(
            archivo=self.archivo_pagos,
            referencia=referencia,
            monto=monto,
            fecha='2026-01-02',
        )

    def test_factura_con_pago_igual_queda_pagada_y_crea_coincidencia_exacta(self):
        factura = self.crear_factura('FAC-001', 100)
        self.crear_pago('FAC-001', 100)
        proceso = ProcesoReconciliacion.objects.create()

        ejecutar_conciliacion(proceso)

        factura.refresh_from_db()
        coincidencia = Coincidencia.objects.get(proceso=proceso, factura=factura)
        self.assertEqual(factura.estado, Factura.EstadoFactura.PAGADA)
        self.assertEqual(coincidencia.tipo, Coincidencia.TipoCoincidencia.EXACTA)

    def test_factura_con_pago_menor_queda_parcial_y_crea_coincidencia_parcial(self):
        factura = self.crear_factura('FAC-002', 100)
        self.crear_pago('FAC-002', 50)
        proceso = ProcesoReconciliacion.objects.create()

        ejecutar_conciliacion(proceso)

        factura.refresh_from_db()
        coincidencia = Coincidencia.objects.get(proceso=proceso, factura=factura)
        self.assertEqual(factura.estado, Factura.EstadoFactura.PARCIAL)
        self.assertEqual(coincidencia.tipo, Coincidencia.TipoCoincidencia.PARCIAL)

    def test_factura_sin_pago_queda_no_encontrada_y_crea_coincidencia_no_encontrada(self):
        factura = self.crear_factura('FAC-003', 100)
        proceso = ProcesoReconciliacion.objects.create()

        ejecutar_conciliacion(proceso)

        factura.refresh_from_db()
        coincidencia = Coincidencia.objects.get(proceso=proceso, factura=factura)
        self.assertEqual(factura.estado, Factura.EstadoFactura.NO_ENCONTRADA)
        self.assertEqual(coincidencia.tipo, Coincidencia.TipoCoincidencia.NO_ENCONTRADA)

    def test_proceso_actualiza_totales_y_estado_finalizado(self):
        self.crear_factura('FAC-004', 100)
        self.crear_factura('FAC-005', 100)
        self.crear_factura('FAC-006', 100)
        self.crear_pago('FAC-004', 100)
        self.crear_pago('FAC-005', 50)
        proceso = ProcesoReconciliacion.objects.create()

        ejecutar_conciliacion(proceso)

        proceso.refresh_from_db()
        self.assertEqual(proceso.total_facturas, 3)
        self.assertEqual(proceso.facturas_conciliadas, 1)
        self.assertEqual(proceso.facturas_pendientes, 2)
        self.assertEqual(proceso.estado, ProcesoReconciliacion.EstadoProceso.FINALIZADO)

    def test_coincidencia_queda_asociada_al_registro_pago_correcto(self):
        factura = self.crear_factura('FAC-007', 100)
        pago = self.crear_pago('FAC-007', 100)
        proceso = ProcesoReconciliacion.objects.create()

        ejecutar_conciliacion(proceso)

        coincidencia = Coincidencia.objects.get(proceso=proceso, factura=factura)
        self.assertEqual(coincidencia.registro_pago, pago)

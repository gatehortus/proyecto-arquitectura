# Autor: Equipo VeriPay
# Comando para generar datos ficticios de prueba
from django.core.management.base import BaseCommand
from django.utils import timezone
from decimal import Decimal
from datetime import date, timedelta
from proveedores.models import Proveedor
from facturas.models import Factura
from pagos.models import ArchivoPagos, RegistroPago
from certificados.models import CertificadoBancario


class Command(BaseCommand):
    help = 'Genera datos ficticios para pruebas del sistema'

    def handle(self, *args, **options):
        self.stdout.write('Generando datos ficticios...')

        # Proveedores
        proveedores_data = [
            ('Distribuciones ABC S.A.S', '900123456-1', 'contacto@abc.com', '3001234567'),
            ('Suministros XYZ Ltda', '800987654-2', 'ventas@xyz.com', '3109876543'),
            ('Importaciones del Valle', '901555666-3', 'info@impvalle.com', '3205556666'),
            ('Tecnología Global S.A', '900777888-4', 'admin@tecglobal.com', '3107778888'),
            ('Papelería El Lápiz', '800333444-5', 'pedidos@ellapiz.com', '3013334444'),
            ('Ferretería Industrial Ltda', '901222333-6', 'ventas@ferreindustrial.com', '3152223333'),
            ('Alimentos del Campo S.A.S', '900444555-7', 'pedidos@alicampo.com', '3204445555'),
            ('Servicios Logísticos Express', '800666777-8', 'operaciones@logexpress.com', '3016667777'),
        ]

        proveedores = []
        for nombre, nit, email, tel in proveedores_data:
            p, _ = Proveedor.objects.get_or_create(nit=nit, defaults={
                'nombre': nombre, 'email': email, 'telefono': tel
            })
            proveedores.append(p)
        self.stdout.write(f'  Proveedores: {len(proveedores)}')

        # Facturas
        facturas_data = [
            (proveedores[0], 'FAC-001', Decimal('1500000'), 'PENDIENTE'),
            (proveedores[0], 'FAC-002', Decimal('2300000'), 'PENDIENTE'),
            (proveedores[1], 'FAC-003', Decimal('800000'), 'PENDIENTE'),
            (proveedores[1], 'FAC-004', Decimal('450000'), 'PENDIENTE'),
            (proveedores[2], 'FAC-005', Decimal('3200000'), 'PENDIENTE'),
            (proveedores[2], 'FAC-006', Decimal('1100000'), 'PENDIENTE'),
            (proveedores[3], 'FAC-007', Decimal('5600000'), 'PENDIENTE'),
            (proveedores[3], 'FAC-008', Decimal('780000'), 'PENDIENTE'),
            (proveedores[4], 'FAC-009', Decimal('250000'), 'PENDIENTE'),
            (proveedores[4], 'FAC-010', Decimal('620000'), 'PENDIENTE'),
            (proveedores[5], 'FAC-011', Decimal('4100000'), 'PENDIENTE'),
            (proveedores[6], 'FAC-012', Decimal('980000'), 'PENDIENTE'),
            (proveedores[6], 'FAC-013', Decimal('1750000'), 'PENDIENTE'),
            (proveedores[7], 'FAC-014', Decimal('3400000'), 'PENDIENTE'),
            (proveedores[7], 'FAC-015', Decimal('560000'), 'PENDIENTE'),
        ]

        facturas = []
        base_date = date.today() - timedelta(days=30)
        for i, (prov, num, monto, estado) in enumerate(facturas_data):
            f, _ = Factura.objects.get_or_create(numero_factura=num, defaults={
                'proveedor': prov,
                'monto_total': monto,
                'monto_pagado': Decimal('0'),
                'fecha_emision': base_date + timedelta(days=i * 2),
                'fecha_vencimiento': base_date + timedelta(days=i * 2 + 30),
                'estado': estado,
            })
            facturas.append(f)
        self.stdout.write(f'  Facturas: {len(facturas)}')

        # Archivo de pagos y registros
        archivo, _ = ArchivoPagos.objects.get_or_create(
            formato='csv',
            procesado=True,
            defaults={
                'total_registros': 10,
                'registros_procesados': 10,
                'procesado_at': timezone.now(),
            }
        )

        registros_data = [
            ('FAC-001', Decimal('1500000'), date.today() - timedelta(days=5), 'Pago factura FAC-001'),
            ('FAC-002', Decimal('2300000'), date.today() - timedelta(days=5), 'Pago factura FAC-002'),
            ('FAC-003', Decimal('800000'), date.today() - timedelta(days=3), 'Pago factura FAC-003'),
            ('FAC-004', Decimal('200000'), date.today() - timedelta(days=3), 'Pago parcial FAC-004'),
            ('FAC-005', Decimal('3200000'), date.today() - timedelta(days=2), 'Pago factura FAC-005'),
            ('FAC-007', Decimal('5600000'), date.today() - timedelta(days=1), 'Pago factura FAC-007'),
            ('FAC-009', Decimal('250000'), date.today() - timedelta(days=1), 'Pago factura FAC-009'),
            ('FAC-011', Decimal('4100000'), date.today(), 'Pago factura FAC-011'),
            ('FAC-012', Decimal('980000'), date.today(), 'Pago factura FAC-012'),
            ('FAC-014', Decimal('3400000'), date.today(), 'Pago factura FAC-014'),
        ]

        for i, (ref, monto, fecha, concepto) in enumerate(registros_data):
            RegistroPago.objects.get_or_create(
                archivo=archivo, referencia=ref, defaults={
                    'monto': monto, 'fecha': fecha, 'concepto': concepto, 'numero_linea': i
                }
            )
        self.stdout.write(f'  Registros de pago: {len(registros_data)}')

        # Certificados bancarios
        certs_data = [
            ('CERT-001', 'Bancolombia', '0012345678', Decimal('1500000'), 'FAC-001', True),
            ('CERT-002', 'Bancolombia', '0012345678', Decimal('2300000'), 'FAC-002', True),
            ('CERT-003', 'Davivienda', '0098765432', Decimal('800000'), 'FAC-003', True),
            ('CERT-004', 'BBVA', '0055667788', Decimal('3200000'), 'FAC-005', False),
            ('CERT-005', 'Banco de Bogotá', '0011223344', Decimal('5600000'), 'FAC-007', True),
            ('CERT-006', 'Bancolombia', '0012345678', Decimal('4100000'), 'FAC-011', True),
            ('CERT-007', 'Davivienda', '0098765432', Decimal('3400000'), 'FAC-014', False),
        ]

        for num, banco, cuenta, monto, ref, verificado in certs_data:
            CertificadoBancario.objects.get_or_create(
                numero_certificado=num, defaults={
                    'banco': banco, 'cuenta_origen': cuenta, 'monto_pagado': monto,
                    'fecha_pago': date.today() - timedelta(days=2),
                    'referencia': ref, 'autenticidad_verificada': verificado,
                }
            )
        self.stdout.write(f'  Certificados: {len(certs_data)}')

        self.stdout.write(self.style.SUCCESS('Datos ficticios generados exitosamente!'))

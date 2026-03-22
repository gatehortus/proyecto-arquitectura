from django.contrib import admin
from .models import ProcesoReconciliacion, Coincidencia
from facturas.models import Factura
from pagos.models import RegistroPago


@admin.action(description="Ejecutar conciliación con pagos")
def ejecutar_conciliacion_basica(modeladmin, request, queryset):
    for proceso in queryset:

        facturas = Factura.objects.all()

        proceso.total_facturas = facturas.count()
        proceso.facturas_conciliadas = 0
        proceso.facturas_pendientes = 0

        for factura in facturas:

            pago = RegistroPago.objects.filter(
                referencia__iexact=factura.numero_factura
            ).first()

            if pago:

                if float(pago.monto) >= float(factura.monto_total):

                    factura.estado = Factura.EstadoFactura.PAGADA
                    tipo = Coincidencia.TipoCoincidencia.EXACTA
                    proceso.facturas_conciliadas += 1

                else:

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
                observacion="Conciliación usando archivo de pagos"
            )

        proceso.estado = ProcesoReconciliacion.EstadoProceso.FINALIZADO
        proceso.save()


@admin.register(ProcesoReconciliacion)
class ProcesoReconciliacionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'estado',
        'tolerancia',
        'total_facturas',
        'facturas_conciliadas',
        'facturas_pendientes',
        'created_at',
    )
    list_filter = ('estado', 'created_at')
    search_fields = ('id',)
    actions = [ejecutar_conciliacion_basica]


@admin.register(Coincidencia)
class CoincidenciaAdmin(admin.ModelAdmin):
    list_display = (
        'factura',
        'proceso',
        'tipo',
        'porcentaje_confianza',
        'created_at',
    )
    list_filter = ('tipo', 'created_at')
    search_fields = (
        'factura__numero_factura',
    )

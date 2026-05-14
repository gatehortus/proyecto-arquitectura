# Autor: Equipo VeriPay
# Vistas de conciliación automática
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.utils.translation import gettext as _

from facturas.models import Factura
from pagos.models import RegistroPago
from certificados.models import CertificadoBancario
from .models import ProcesoReconciliacion, Coincidencia
from .services import run_reconciliation
from core.services.pdf_generator import generate_conciliacion_report


class ProcesoListView(LoginRequiredMixin, ListView):
    model = ProcesoReconciliacion
    template_name = 'conciliacion/list.html'
    paginate_by = 15
    ordering = ['-created_at']


class ProcesoDetailView(LoginRequiredMixin, DetailView):
    model = ProcesoReconciliacion
    template_name = 'conciliacion/detail.html'
    context_object_name = 'proceso'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['coincidencias'] = Coincidencia.objects.filter(
            proceso=self.object
        ).select_related('factura', 'factura__proveedor', 'registro_pago')
        return ctx


class RunReconciliacionView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        context = {
            'facturas_pendientes': Factura.objects.filter(
                estado__in=['PENDIENTE', 'PARCIAL', 'NO_ENCONTRADA']
            ).count(),
            'registros_pago': RegistroPago.objects.count(),
            'certificados': CertificadoBancario.objects.count(),
        }
        return render(request, 'conciliacion/run.html', context)

    def post(self, request):
        tolerancia = int(request.POST.get('tolerancia', 5))
        proceso = run_reconciliation(tolerancia=tolerancia)
        messages.success(
            request,
            _("Conciliación finalizada: %(conciliadas)s/%(total)s facturas conciliadas.") % {
                "conciliadas": proceso.facturas_conciliadas,
                "total": proceso.total_facturas,
            }
        )
        return redirect('conciliacion_detail', pk=proceso.id)


class ProcesoReportPDFView(LoginRequiredMixin, View):
    def get(self, request, pk):
        proceso = get_object_or_404(ProcesoReconciliacion, pk=pk)
        pdf_buffer = generate_conciliacion_report(proceso)
        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        filename = _("conciliacion_%(id)s.pdf") % {"id": proceso.id}
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

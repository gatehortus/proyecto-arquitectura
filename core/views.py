# Autor: Equipo VeriPay
# Vistas principales: Dashboard, Login, Reportes, Email
import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from django.db.models import Sum, Count, Q
from django.utils.translation import gettext as _

from proveedores.models import Proveedor
from facturas.models import Factura
from pagos.models import RegistroPago
from conciliacion.models import ProcesoReconciliacion
from core.services.pdf_generator import (
    generate_facturas_report, generate_conciliacion_report, generate_proveedores_report
)
from core.services.email_service import send_reconciliation_summary


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        facturas = Factura.objects.all()
        monto_pendiente = facturas.filter(
            estado__in=['PENDIENTE', 'PARCIAL']
        ).aggregate(total=Sum('monto_total'))['total'] or 0

        # Datos para gráfico de estados
        status_counts = facturas.values('estado').annotate(count=Count('id'))
        labels_map = dict(Factura.ESTADO_CHOICES) if hasattr(Factura, 'ESTADO_CHOICES') else {}
        status_data = {
            'labels': [labels_map.get(s['estado'], s['estado']) for s in status_counts],
            'values': [s['count'] for s in status_counts],
        }

        # Datos para gráfico de pagos
        pagos = RegistroPago.objects.order_by('-fecha')[:30]
        pagos_agrupados = {}
        for p in pagos:
            key = p.fecha.strftime('%d/%m') if p.fecha else 'N/A'
            pagos_agrupados[key] = pagos_agrupados.get(key, 0) + float(p.monto)
        pagos_data = {
            'labels': list(pagos_agrupados.keys())[:10],
            'values': list(pagos_agrupados.values())[:10],
        }

        context = {
            'total_proveedores': Proveedor.objects.count(),
            'facturas_pendientes': facturas.filter(estado='PENDIENTE').count(),
            'monto_pendiente': monto_pendiente,
            'total_conciliaciones': ProcesoReconciliacion.objects.count(),
            'ultimas_facturas': facturas.select_related('proveedor').order_by('-created_at')[:5],
            'ultimas_conciliaciones': ProcesoReconciliacion.objects.order_by('-created_at')[:5],
            'status_data': json.dumps(status_data),
            'pagos_data': json.dumps(pagos_data),
        }
        return render(request, 'dashboard/index.html', context)


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'auth/login.html', {'form': None})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'auth/login.html', {'form': {'errors': True}})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')


class ReportsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'reports/index.html')

    def post(self, request):
        tipo = request.POST.get('tipo', 'facturas')
        fecha_desde = request.POST.get('fecha_desde')
        fecha_hasta = request.POST.get('fecha_hasta')

        if tipo == 'facturas':
            qs = Factura.objects.select_related('proveedor').all()
            if fecha_desde:
                qs = qs.filter(fecha_emision__gte=fecha_desde)
            if fecha_hasta:
                qs = qs.filter(fecha_emision__lte=fecha_hasta)
            pdf_buffer = generate_facturas_report(qs)
        elif tipo == 'conciliacion':
            proceso = ProcesoReconciliacion.objects.order_by('-created_at').first()
            if not proceso:
                messages.warning(request, _("No hay conciliaciones para reportar."))
                return redirect('reports')
            pdf_buffer = generate_conciliacion_report(proceso)
        else:
            qs = Proveedor.objects.all()
            pdf_buffer = generate_proveedores_report(qs)

        response = HttpResponse(pdf_buffer, content_type='application/pdf')
        filename = _("reporte_%(tipo)s.pdf") % {"tipo": tipo}
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response


class EmailSummaryView(LoginRequiredMixin, View):
    def get(self, request):
        proveedores = Proveedor.objects.all()
        return render(request, 'email/summary_form.html', {'proveedores': proveedores})

    def post(self, request):
        destinatarios_raw = request.POST.get('destinatarios', '')
        destinatarios = [e.strip() for e in destinatarios_raw.split(',') if e.strip()]

        if not destinatarios:
            messages.error(request, _("Debe ingresar al menos un correo destinatario."))
            return redirect('email_summary')

        proveedor_id = request.POST.get('proveedor')
        facturas_qs = Factura.objects.all()
        if proveedor_id:
            facturas_qs = facturas_qs.filter(proveedor_id=proveedor_id)

        facturas_resumen = facturas_qs.filter(estado__in=['PENDIENTE', 'PARCIAL'])[:20]
        conciliacion_resumen = ProcesoReconciliacion.objects.order_by('-created_at').first()

        success = send_reconciliation_summary(
            destinatarios=destinatarios,
            facturas_resumen=facturas_resumen if 'incluir_facturas' in request.POST else None,
            conciliacion_resumen=conciliacion_resumen if 'incluir_conciliacion' in request.POST else None,
        )

        if success:
            messages.success(
                request,
                _("Resumen enviado a %(destinatarios)s") % {
                    "destinatarios": ", ".join(destinatarios)
                }
            )
        else:
            messages.warning(
                request,
                _("El correo se configuró pero no se pudo enviar (verifique configuración SMTP).")
            )
        return redirect('email_summary')

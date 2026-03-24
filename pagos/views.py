# Autor: Equipo VeriPay
# Vistas de carga y procesamiento de archivos de pagos
import csv
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import ArchivoPagos, RegistroPago
from .forms import ArchivoPagosUploadForm


class ArchivoPagosListView(LoginRequiredMixin, ListView):
    model = ArchivoPagos
    template_name = 'pagos/list.html'
    paginate_by = 15
    ordering = ['-created_at']


class PagosUploadView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        return render(request, 'pagos/upload.html', {'form': ArchivoPagosUploadForm()})

    def post(self, request):
        form = ArchivoPagosUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_pago = form.save(commit=False)
            archivo_pago.total_registros = 0
            archivo_pago.registros_procesados = 0
            archivo_pago.procesado = False
            archivo_pago.save()
            _process_file(archivo_pago)
            messages.success(request, f'Archivo cargado y procesado: {archivo_pago.total_registros} registros.')
            return redirect('pagos_list')
        return render(request, 'pagos/upload.html', {'form': form})


class PagosProcessView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, pk):
        archivo_pago = get_object_or_404(ArchivoPagos, pk=pk)
        if not archivo_pago.procesado:
            _process_file(archivo_pago)
            messages.success(request, f'Archivo procesado: {archivo_pago.total_registros} registros.')
        return redirect('pagos_list')


class RegistrosPagoListView(LoginRequiredMixin, View):
    def get(self, request, pk):
        archivo = get_object_or_404(ArchivoPagos, pk=pk)
        registros = RegistroPago.objects.filter(archivo=archivo).order_by('numero_linea')
        return render(request, 'pagos/registros.html', {'archivo': archivo, 'registros': registros})


def _process_file(archivo_pago):
    """Procesa un archivo CSV de pagos."""
    if not archivo_pago.archivo:
        return
    try:
        ruta = archivo_pago.archivo.path
        with open(ruta, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            contador = 0
            for fila in reader:
                RegistroPago.objects.create(
                    archivo=archivo_pago,
                    referencia=fila.get('referencia', ''),
                    monto=fila.get('monto', 0),
                    fecha=fila.get('fecha', None),
                    concepto=fila.get('concepto', ''),
                    numero_linea=contador,
                )
                contador += 1
        archivo_pago.total_registros = contador
        archivo_pago.registros_procesados = contador
        archivo_pago.procesado = True
        archivo_pago.save()
    except Exception:
        archivo_pago.procesado = False
        archivo_pago.save()

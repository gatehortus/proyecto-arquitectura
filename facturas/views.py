# Autor: Equipo VeriPay
# Vistas CRUD de facturas + OCR
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q
from .models import Factura
from .forms import FacturaForm, OCRUploadForm
from .services import process_invoice_image
from conciliacion.models import Coincidencia


class FacturaListView(LoginRequiredMixin, ListView):
    model = Factura
    template_name = 'facturas/list.html'
    paginate_by = 15

    def get_queryset(self):
        qs = Factura.objects.select_related('proveedor').all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(numero_factura__icontains=q) | Q(proveedor__nombre__icontains=q))
        estado = self.request.GET.get('estado')
        if estado:
            qs = qs.filter(estado=estado)
        fecha_desde = self.request.GET.get('fecha_desde')
        if fecha_desde:
            qs = qs.filter(fecha_emision__gte=fecha_desde)
        fecha_hasta = self.request.GET.get('fecha_hasta')
        if fecha_hasta:
            qs = qs.filter(fecha_emision__lte=fecha_hasta)
        return qs.order_by('-created_at')


class FacturaDetailView(LoginRequiredMixin, DetailView):
    model = Factura
    template_name = 'facturas/detail.html'
    context_object_name = 'factura'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['coincidencias'] = Coincidencia.objects.filter(
            factura=self.object
        ).select_related('registro_pago')
        return ctx


class FacturaCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'facturas/form.html'
    success_url = reverse_lazy('factura_list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = 'Nueva Factura'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Factura creada exitosamente.')
        return super().form_valid(form)


class FacturaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'facturas/form.html'
    success_url = reverse_lazy('factura_list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = f'Editar: {self.object.numero_factura}'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Factura actualizada.')
        return super().form_valid(form)


class OCRUploadView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        return render(request, 'facturas/ocr_upload.html', {'form': OCRUploadForm()})

    def post(self, request):
        form = OCRUploadForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = request.FILES['imagen']
            result = process_invoice_image(imagen)
            initial = {
                'numero_factura': result.get('numero_factura', ''),
                'monto_total': result.get('monto_total', ''),
                'fecha_emision': result.get('fecha_emision', ''),
            }
            factura_form = FacturaForm(initial=initial)
            return render(request, 'facturas/ocr_result.html', {
                'form': factura_form,
                'raw_text': result['raw_text'],
                'confidence': result['confidence'],
            })
        return render(request, 'facturas/ocr_upload.html', {'form': form})


class OCRConfirmView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def post(self, request):
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Factura creada desde OCR exitosamente.')
            return redirect('factura_list')
        return render(request, 'facturas/ocr_result.html', {
            'form': form, 'raw_text': '', 'confidence': 0
        })

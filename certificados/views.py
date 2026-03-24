# Autor: Equipo VeriPay
# Vistas CRUD de certificados bancarios
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from .models import CertificadoBancario
from .forms import CertificadoForm


class CertificadoListView(LoginRequiredMixin, ListView):
    model = CertificadoBancario
    template_name = 'certificados/list.html'
    paginate_by = 15

    def get_queryset(self):
        qs = CertificadoBancario.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(numero_certificado__icontains=q) | Q(banco__icontains=q))
        return qs.order_by('-created_at')


class CertificadoDetailView(LoginRequiredMixin, DetailView):
    model = CertificadoBancario
    template_name = 'certificados/detail.html'
    context_object_name = 'cert'


class CertificadoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CertificadoBancario
    form_class = CertificadoForm
    template_name = 'certificados/form.html'
    success_url = reverse_lazy('certificado_list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = 'Nuevo Certificado Bancario'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Certificado creado exitosamente.')
        return super().form_valid(form)


class CertificadoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CertificadoBancario
    form_class = CertificadoForm
    template_name = 'certificados/form.html'
    success_url = reverse_lazy('certificado_list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = f'Editar: {self.object.numero_certificado}'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Certificado actualizado.')
        return super().form_valid(form)

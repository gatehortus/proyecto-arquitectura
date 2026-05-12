# Autor: Equipo VeriPay
# Vistas CRUD de proveedores
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.db.models import Q, Count
from .models import Proveedor
from .forms import ProveedorForm


@login_required
def proveedores_publicos(request):
    proveedores = list(
        Proveedor.objects.order_by('nombre').values(
            'id',
            'nombre',
            'nit',
            'email',
        )
    )
    return JsonResponse(proveedores, safe=False)


class ProveedorListView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'proveedores/list.html'
    paginate_by = 15

    def get_queryset(self):
        qs = Proveedor.objects.annotate(facturas_count=Count('facturas'))
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(nombre__icontains=q) | Q(nit__icontains=q))
        return qs.order_by('-created_at')


class ProveedorDetailView(LoginRequiredMixin, DetailView):
    model = Proveedor
    template_name = 'proveedores/detail.html'
    context_object_name = 'proveedor'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['facturas'] = self.object.facturas.all().order_by('-fecha_emision')
        return ctx


class ProveedorCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/form.html'
    success_url = reverse_lazy('proveedor_list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = 'Nuevo Proveedor'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Proveedor creado exitosamente.')
        return super().form_valid(form)


class ProveedorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'proveedores/form.html'
    success_url = reverse_lazy('proveedor_list')

    def test_func(self):
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_title'] = f'Editar: {self.object.nombre}'
        return ctx

    def form_valid(self, form):
        messages.success(self.request, 'Proveedor actualizado.')
        return super().form_valid(form)


class ProveedorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedor_list')

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Proveedor eliminado.')
        return self.delete(request, *args, **kwargs)

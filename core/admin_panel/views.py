# Autor: Equipo VeriPay
# Vistas del panel de administración
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views import View
from django import forms
from django.utils.translation import gettext as _


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AdminDashboardView(StaffRequiredMixin, View):
    def get(self, request):
        users = User.objects.all().order_by('-date_joined')
        context = {
            'users': users,
            'total_users': users.count(),
            'active_users': users.filter(is_active=True).count(),
            'staff_users': users.filter(is_staff=True).count(),
        }
        return render(request, 'admin_panel/dashboard.html', context)


class AdminUserCreateView(StaffRequiredMixin, View):
    def get(self, request):
        form = UserCreationForm()
        # Agregar clases CSS a los campos
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        return render(request, 'admin_panel/user_form.html', {
            'form': form, 'form_title': _("Crear Usuario")
        })

    def post(self, request):
        form = UserCreationForm(request.POST)
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
        if form.is_valid():
            form.save()
            messages.success(request, _("Usuario creado exitosamente."))
            return redirect('admin_dashboard')
        return render(request, 'admin_panel/user_form.html', {
            'form': form, 'form_title': _("Crear Usuario")
        })


class AdminUserEditView(StaffRequiredMixin, View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserEditForm(instance=user)
        return render(request, 'admin_panel/user_form.html', {
            'form': form,
            'form_title': _("Editar Usuario: %(username)s") % {
                "username": user.username
            }
        })

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, _("Usuario actualizado."))
            return redirect('admin_dashboard')
        return render(request, 'admin_panel/user_form.html', {
            'form': form,
            'form_title': _("Editar Usuario: %(username)s") % {
                "username": user.username
            }
        })

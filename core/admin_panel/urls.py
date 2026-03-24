# Autor: Equipo VeriPay
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('usuarios/crear/', views.AdminUserCreateView.as_view(), name='admin_user_create'),
    path('usuarios/<int:pk>/editar/', views.AdminUserEditView.as_view(), name='admin_user_edit'),
]

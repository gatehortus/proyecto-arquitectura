# Autor: Equipo VeriPay
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProveedorListView.as_view(), name='proveedor_list'),
    path('crear/', views.ProveedorCreateView.as_view(), name='proveedor_create'),
    path('<uuid:pk>/', views.ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('<uuid:pk>/editar/', views.ProveedorUpdateView.as_view(), name='proveedor_edit'),
    path('<uuid:pk>/eliminar/', views.ProveedorDeleteView.as_view(), name='proveedor_delete'),
]

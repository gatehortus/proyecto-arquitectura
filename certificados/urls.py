# Autor: Equipo VeriPay
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CertificadoListView.as_view(), name='certificado_list'),
    path('crear/', views.CertificadoCreateView.as_view(), name='certificado_create'),
    path('<uuid:pk>/', views.CertificadoDetailView.as_view(), name='certificado_detail'),
    path('<uuid:pk>/editar/', views.CertificadoUpdateView.as_view(), name='certificado_edit'),
]

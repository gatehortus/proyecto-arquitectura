# Autor: Equipo VeriPay
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArchivoPagosListView.as_view(), name='pagos_list'),
    path('cargar/', views.PagosUploadView.as_view(), name='pagos_upload'),
    path('<uuid:pk>/procesar/', views.PagosProcessView.as_view(), name='pagos_process'),
    path('<uuid:pk>/registros/', views.RegistrosPagoListView.as_view(), name='pagos_registros'),
]

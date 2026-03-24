# Autor: Equipo VeriPay
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProcesoListView.as_view(), name='conciliacion_list'),
    path('ejecutar/', views.RunReconciliacionView.as_view(), name='conciliacion_run'),
    path('<uuid:pk>/', views.ProcesoDetailView.as_view(), name='conciliacion_detail'),
    path('<uuid:pk>/pdf/', views.ProcesoReportPDFView.as_view(), name='conciliacion_pdf'),
]

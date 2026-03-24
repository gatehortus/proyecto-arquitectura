# Autor: Equipo VeriPay
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FacturaListView.as_view(), name='factura_list'),
    path('crear/', views.FacturaCreateView.as_view(), name='factura_create'),
    path('ocr/', views.OCRUploadView.as_view(), name='factura_ocr_upload'),
    path('ocr/confirmar/', views.OCRConfirmView.as_view(), name='factura_ocr_confirm'),
    path('<uuid:pk>/', views.FacturaDetailView.as_view(), name='factura_detail'),
    path('<uuid:pk>/editar/', views.FacturaUpdateView.as_view(), name='factura_edit'),
]

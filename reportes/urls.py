from django.urls import path

from . import views


urlpatterns = [
    path('generar/', views.generar_reporte, name='generar_reporte'),
]

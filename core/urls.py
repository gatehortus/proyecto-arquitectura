# Autor: Equipo VeriPay
from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('reportes/', views.ReportsView.as_view(), name='reports'),
    path('email-resumen/', views.EmailSummaryView.as_view(), name='email_summary'),
    path('aliados/', views.AliadosView.as_view(), name='aliados'),
    path('cambiar-idioma/', views.SwitchLanguageView.as_view(), name='switch_language'),
]

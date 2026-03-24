# Autor: Equipo VeriPay
from django import forms
from .models import CertificadoBancario


class CertificadoForm(forms.ModelForm):
    class Meta:
        model = CertificadoBancario
        fields = ['numero_certificado', 'banco', 'cuenta_origen', 'monto_pagado',
                  'fecha_pago', 'referencia', 'autenticidad_verificada']
        widgets = {
            'numero_certificado': forms.TextInput(attrs={'class': 'form-control'}),
            'banco': forms.TextInput(attrs={'class': 'form-control'}),
            'cuenta_origen': forms.TextInput(attrs={'class': 'form-control'}),
            'monto_pagado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_pago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'autenticidad_verificada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Autor: Equipo VeriPay
from django import forms
from .models import Factura


class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['proveedor', 'numero_factura', 'uuid_fiscal', 'monto_total',
                  'monto_pagado', 'fecha_emision', 'fecha_vencimiento', 'estado']
        widgets = {
            'proveedor': forms.Select(attrs={'class': 'form-select'}),
            'numero_factura': forms.TextInput(attrs={'class': 'form-control'}),
            'uuid_fiscal': forms.TextInput(attrs={'class': 'form-control'}),
            'monto_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'monto_pagado': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_vencimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-select'}),
        }


class OCRUploadForm(forms.Form):
    imagen = forms.ImageField(
        label='Imagen de factura',
        help_text='Formatos: JPG, PNG. Máximo 10MB.'
    )

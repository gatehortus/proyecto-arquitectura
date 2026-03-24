# Autor: Equipo VeriPay
from django import forms
from .models import ArchivoPagos


class ArchivoPagosUploadForm(forms.ModelForm):
    class Meta:
        model = ArchivoPagos
        fields = ['archivo', 'formato']
        widgets = {
            'archivo': forms.FileInput(attrs={'class': 'form-control', 'accept': '.csv,.xlsx'}),
            'formato': forms.Select(
                choices=[('csv', 'CSV'), ('xlsx', 'Excel XLSX')],
                attrs={'class': 'form-select'}
            ),
        }

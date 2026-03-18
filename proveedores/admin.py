from django.contrib import admin
from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit', 'email', 'telefono', 'created_at')
    search_fields = ('nombre', 'nit', 'email')

# Register your models here.

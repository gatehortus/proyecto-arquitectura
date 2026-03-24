# Autor: Equipo VeriPay
from django import template
from django.utils.formats import number_format

register = template.Library()


@register.filter
def currency(value):
    """Formato moneda: {{ monto|currency }} -> $1,234.56"""
    try:
        return f"${number_format(float(value), 2)}"
    except (ValueError, TypeError):
        return value

# Autor: Equipo VeriPay
from django import template
from django.conf import settings
from django.utils.formats import number_format

register = template.Library()


@register.filter
def currency(value):
    try:
        return f"${number_format(float(value), 2)}"
    except (ValueError, TypeError):
        return value


@register.simple_tag
def strip_lang_prefix(path):
    if not path:
        return '/'
    codes = [code for code, _name in getattr(settings, 'LANGUAGES', [])]
    for code in codes:
        prefix = f'/{code}/'
        if path.startswith(prefix):
            return '/' + path[len(prefix):]
        if path == f'/{code}':
            return '/'
    return path

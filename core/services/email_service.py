# Autor: Equipo VeriPay
# Servicio de envío de resúmenes por correo electrónico
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_reconciliation_summary(destinatarios, facturas_resumen=None, conciliacion_resumen=None):
    """
    Envía un resumen de conciliación por correo electrónico.
    destinatarios: lista de emails
    """
    context = {
        'facturas_resumen': facturas_resumen,
        'conciliacion_resumen': conciliacion_resumen,
    }
    html_message = render_to_string('email/email_template.html', context)

    try:
        send_mail(
            subject='VeriPay — Resumen de Estado de Pagos',
            message='Resumen de estado de pagos generado por VeriPay.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=destinatarios,
            html_message=html_message,
            fail_silently=False,
        )
        return True
    except Exception:
        return False

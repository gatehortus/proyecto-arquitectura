# Autor: Equipo VeriPay
# Generador de reportes PDF con reportlab
from io import BytesIO
from django.utils import timezone
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer


def _build_pdf(titulo, columnas, filas, resumen=None):
    """Genera un PDF con tabla y resumen."""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    styles = getSampleStyleSheet()
    elements = []

    # Título
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=18, textColor=colors.HexColor('#1e293b'))
    elements.append(Paragraph(f'VeriPay — {titulo}', title_style))
    elements.append(Paragraph(f'Generado: {timezone.now().strftime("%d/%m/%Y %H:%M")}', styles['Normal']))
    elements.append(Spacer(1, 20))

    # Resumen
    if resumen:
        resumen_text = ' | '.join([f'{item["label"]}: {item["valor"]}' for item in resumen])
        elements.append(Paragraph(f'<b>Resumen:</b> {resumen_text}', styles['Normal']))
        elements.append(Spacer(1, 15))

    # Tabla
    data = [columnas] + filas
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8fafc')]),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    elements.append(table)

    # Footer
    elements.append(Spacer(1, 30))
    footer_style = ParagraphStyle('Footer', parent=styles['Normal'], fontSize=8, textColor=colors.grey)
    elements.append(Paragraph('VeriPay — Sistema de Conciliación Automática de Pagos', footer_style))

    doc.build(elements)
    buffer.seek(0)
    return buffer


def generate_facturas_report(facturas):
    """Genera reporte PDF de facturas."""
    filas = [
        [f.numero_factura, f.proveedor.nombre,
         f'${f.monto_total:,.0f}', f'${f.monto_pagado:,.0f}',
         f.get_estado_display()]
        for f in facturas
    ]
    resumen = [
        {'label': 'Total Facturas', 'valor': facturas.count()},
        {'label': 'Monto Total', 'valor': f"${sum(f.monto_total for f in facturas):,.0f}"},
    ]
    return _build_pdf('Reporte de Facturas',
                       ['Número', 'Proveedor', 'Monto Total', 'Monto Pagado', 'Estado'],
                       filas, resumen)


def generate_conciliacion_report(proceso):
    """Genera reporte PDF de un proceso de conciliación."""
    coincidencias = proceso.coincidencia_set.select_related('factura', 'factura__proveedor')
    filas = [
        [c.factura.numero_factura, c.factura.proveedor.nombre,
         f'${c.factura.monto_total:,.0f}', c.get_tipo_display(),
         f'{c.porcentaje_confianza}%']
        for c in coincidencias
    ]
    resumen = [
        {'label': 'Total', 'valor': proceso.total_facturas},
        {'label': 'Conciliadas', 'valor': proceso.facturas_conciliadas},
        {'label': 'Pendientes', 'valor': proceso.facturas_pendientes},
    ]
    return _build_pdf(f'Reporte de Conciliación — {proceso.created_at.strftime("%d/%m/%Y")}',
                       ['Factura', 'Proveedor', 'Monto', 'Tipo', 'Confianza'],
                       filas, resumen)


def generate_proveedores_report(proveedores):
    """Genera reporte PDF de proveedores."""
    filas = [
        [p.nombre, p.nit, p.email or '-', p.telefono or '-',
         str(p.facturas.count())]
        for p in proveedores
    ]
    resumen = [{'label': 'Total Proveedores', 'valor': proveedores.count()}]
    return _build_pdf('Reporte de Proveedores',
                       ['Nombre', 'NIT', 'Email', 'Teléfono', 'Facturas'],
                       filas, resumen)

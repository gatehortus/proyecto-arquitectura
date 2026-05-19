from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .services.report_generators import (
    ExcelReportGenerator,
    PDFReportGenerator,
    ReportGenerator,
)


GENERATORS = {
    'pdf': PDFReportGenerator,
    'excel': ExcelReportGenerator,
}


def get_report_generator(formato) -> ReportGenerator:
    generator_class = GENERATORS.get(formato, PDFReportGenerator)
    return generator_class()


@login_required
def generar_reporte(request):
    tipo = request.GET.get('tipo', 'facturas')
    formato = request.GET.get('formato', 'pdf')
    generator = get_report_generator(formato)
    contenido, filename, mime = generator.generate({
        'tipo': tipo,
        'fecha_desde': request.GET.get('fecha_desde'),
        'fecha_hasta': request.GET.get('fecha_hasta'),
    })
    response = HttpResponse(contenido, content_type=mime)
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response

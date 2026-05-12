from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .services.report_generators import ExcelReportGenerator, PDFReportGenerator


def get_report_generator(tipo):
    generators = {
        'pdf': PDFReportGenerator,
        'excel': ExcelReportGenerator,
    }
    generator_class = generators.get(tipo, PDFReportGenerator)
    return generator_class()


@login_required
def generar_reporte(request):
    tipo = request.GET.get('tipo')
    data = [
        {'id': 1, 'nombre': 'Proveedor Demo'},
        {'id': 2, 'nombre': 'Factura Demo'},
    ]
    generator = get_report_generator(tipo)
    result = generator.generate(data)
    return JsonResponse(result)

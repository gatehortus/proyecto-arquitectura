from abc import ABC, abstractmethod
from django.utils.translation import gettext as _


class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, data):
        pass


class PDFReportGenerator(ReportGenerator):
    def generate(self, data):
        data = [] if data is None else data
        return {
            'type': 'pdf',
            'filename': _("report.pdf"),
            'content': _("Reporte PDF generado con %(total)s registros.") % {
                "total": len(data)
            },
        }


class ExcelReportGenerator(ReportGenerator):
    def generate(self, data):
        data = [] if data is None else data
        return {
            'type': 'excel',
            'filename': _("report.xlsx"),
            'content': _("Reporte Excel generado con %(total)s registros.") % {
                "total": len(data)
            },
        }

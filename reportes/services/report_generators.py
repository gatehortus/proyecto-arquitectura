from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, data):
        pass


class PDFReportGenerator(ReportGenerator):
    def generate(self, data):
        data = [] if data is None else data
        return {
            'type': 'pdf',
            'filename': 'report.pdf',
            'content': f'Reporte PDF generado con {len(data)} registros.',
        }


class ExcelReportGenerator(ReportGenerator):
    def generate(self, data):
        data = [] if data is None else data
        return {
            'type': 'excel',
            'filename': 'report.xlsx',
            'content': f'Reporte Excel generado con {len(data)} registros.',
        }

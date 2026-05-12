from django.test import TestCase

from .services.report_generators import ExcelReportGenerator, PDFReportGenerator
from .views import get_report_generator


class ReportGeneratorTests(TestCase):
    def test_get_report_generator_returns_pdf_generator(self):
        generator = get_report_generator('pdf')

        self.assertIsInstance(generator, PDFReportGenerator)

    def test_get_report_generator_returns_excel_generator(self):
        generator = get_report_generator('excel')

        self.assertIsInstance(generator, ExcelReportGenerator)

    def test_get_report_generator_defaults_to_pdf_generator(self):
        generator = get_report_generator('otro')

        self.assertIsInstance(generator, PDFReportGenerator)

    def test_pdf_report_generator_generate_returns_pdf_type(self):
        result = PDFReportGenerator().generate([{'id': 1}])

        self.assertEqual(result['type'], 'pdf')

    def test_excel_report_generator_generate_returns_excel_type(self):
        result = ExcelReportGenerator().generate([{'id': 1}])

        self.assertEqual(result['type'], 'excel')

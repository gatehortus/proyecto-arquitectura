from django.test import TestCase

from .services.report_generators import (
    ExcelReportGenerator,
    PDFReportGenerator,
    ReportGenerator,
)


class InversionDeDependenciasTests(TestCase):
    def test_pdf_generator_implementa_interfaz_y_produce_pdf_real(self):
        generator = PDFReportGenerator()
        self.assertIsInstance(generator, ReportGenerator)
        contenido, filename, mime = generator.generate({'tipo': 'proveedores'})
        self.assertEqual(mime, 'application/pdf')
        self.assertTrue(filename.endswith('.pdf'))
        self.assertTrue(contenido.startswith(b'%PDF'))

    def test_excel_generator_implementa_interfaz_y_produce_xlsx_real(self):
        generator = ExcelReportGenerator()
        self.assertIsInstance(generator, ReportGenerator)
        contenido, filename, mime = generator.generate({'tipo': 'proveedores'})
        self.assertEqual(
            mime,
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        )
        self.assertTrue(filename.endswith('.xlsx'))
        self.assertTrue(contenido.startswith(b'PK'))

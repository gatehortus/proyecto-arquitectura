# Autor: Equipo VeriPay
# Servicio OCR para extracción de datos de facturas
import re
from PIL import Image, ImageEnhance, ImageFilter

try:
    import pytesseract
except ImportError:
    pytesseract = None


def process_invoice_image(image_file):
    """
    Procesa una imagen de factura con OCR y extrae datos relevantes.
    Retorna dict con campos extraídos, texto crudo y confianza.
    """
    if not pytesseract:
        return {
            'raw_text': 'OCR no disponible (pytesseract no instalado)',
            'confidence': 0,
            'numero_factura': '',
            'monto_total': '',
            'fecha_emision': '',
        }

    img = Image.open(image_file)
    # Preprocesamiento para mejorar OCR
    img = img.convert('L')  # Escala de grises
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = img.filter(ImageFilter.SHARPEN)

    # Extraer texto con datos de confianza
    data = pytesseract.image_to_data(img, lang='spa', output_type=pytesseract.Output.DICT)
    raw_text = pytesseract.image_to_string(img, lang='spa')

    # Calcular confianza promedio
    confidences = [int(c) for c in data.get('conf', []) if int(c) > 0]
    avg_confidence = sum(confidences) / len(confidences) if confidences else 0

    # Extraer campos con regex
    extracted = {
        'raw_text': raw_text,
        'confidence': round(avg_confidence),
        'numero_factura': _extract_invoice_number(raw_text),
        'monto_total': _extract_amount(raw_text),
        'fecha_emision': _extract_date(raw_text),
    }
    return extracted


def _extract_invoice_number(text):
    """Busca patrones de número de factura."""
    patterns = [
        r'(?:factura|fact|fac|invoice|no\.?)\s*[:#]?\s*([A-Z0-9][\w-]{2,20})',
        r'(?:N[°ºo]\.?\s*)([A-Z0-9][\w-]{2,20})',
        r'\b(FAC-\d+)\b',
        r'\b(FV-\d+)\b',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return ''


def _extract_amount(text):
    """Busca patrones de monto total."""
    patterns = [
        r'(?:total|monto|valor|amount)\s*[:]?\s*\$?\s*([\d.,]+)',
        r'\$\s*([\d.,]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            amount_str = match.group(1).replace('.', '').replace(',', '.')
            try:
                return str(float(amount_str))
            except ValueError:
                continue
    return ''


def _extract_date(text):
    """Busca patrones de fecha."""
    patterns = [
        r'(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        r'(\d{4}[/-]\d{1,2}[/-]\d{1,2})',
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)
    return ''

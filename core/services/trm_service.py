import requests
from datetime import datetime
from django.core.cache import cache

TRM_URL = (
    'https://www.datos.gov.co/resource/32sa-8pi3.json'
    '?$limit=1&$order=vigenciadesde DESC'
)
CACHE_KEY = 'veripay:trm:cop_usd'
CACHE_TTL = 3600


def get_current_trm():
    cached = cache.get(CACHE_KEY)
    if cached is not None:
        return cached
    try:
        response = requests.get(TRM_URL, timeout=4)
        response.raise_for_status()
        payload = response.json()
        if not payload:
            return None
        item = payload[0]
        valor = float(item.get('valor', 0))
        if valor <= 0:
            return None
        desde = item.get('vigenciadesde', '')[:10]
        data = {
            'valor': round(valor, 2),
            'valor_formateado': f"${valor:,.2f}",
            'fuente': 'Superfinanciera de Colombia',
            'vigencia_desde': desde,
            'fecha_consulta': datetime.now().strftime('%d/%m/%Y %H:%M'),
        }
        cache.set(CACHE_KEY, data, CACHE_TTL)
        return data
    except (requests.RequestException, ValueError, KeyError):
        return None

import requests
from django.conf import settings
from django.core.cache import cache

CACHE_KEY = 'veripay:aliados:items'
CACHE_TTL = 300


def is_aliados_configured():
    url = getattr(settings, 'EQUIPO_PREVIO_API_URL', '') or ''
    return bool(url.strip())


def fetch_aliados():
    if not is_aliados_configured():
        return {'items': [], 'configured': False, 'error': None}

    cached = cache.get(CACHE_KEY)
    if cached is not None:
        return cached

    url = settings.EQUIPO_PREVIO_API_URL
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        payload = response.json()
        items = payload if isinstance(payload, list) else payload.get('results') or payload.get('data') or []
        result = {'items': items, 'configured': True, 'error': None}
        cache.set(CACHE_KEY, result, CACHE_TTL)
        return result
    except requests.RequestException as exc:
        return {'items': [], 'configured': True, 'error': str(exc)}
    except ValueError:
        return {'items': [], 'configured': True, 'error': 'invalid-json'}

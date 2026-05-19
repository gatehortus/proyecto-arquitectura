from core.services.trm_service import get_current_trm
from core.services.aliados_client import is_aliados_configured


def trm(request):
    return {
        'trm_cop_usd': get_current_trm(),
        'aliados_configured': is_aliados_configured(),
    }

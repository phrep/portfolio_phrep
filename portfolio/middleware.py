from django.core.cache import cache
from django.http import HttpResponse

from .utils import get_client_ip

ADMIN_LOGIN_MAX_ATTEMPTS = 5
ADMIN_LOGIN_WINDOW = 300  # segundos


def record_failed_admin_login(request):
    key = f'admin_login_rate:{get_client_ip(request)}'
    if not cache.add(key, 1, timeout=ADMIN_LOGIN_WINDOW):
        cache.incr(key)


class AdminLoginThrottleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/admin/login/' and request.method == 'POST':
            key = f'admin_login_rate:{get_client_ip(request)}'
            if cache.get(key, 0) >= ADMIN_LOGIN_MAX_ATTEMPTS:
                return HttpResponse(
                    'Muitas tentativas de login. Tente novamente em alguns minutos.',
                    status=429,
                )
        return self.get_response(request)

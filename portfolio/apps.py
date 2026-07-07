from django.apps import AppConfig
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"

    def ready(self):
        from .middleware import record_failed_admin_login

        @receiver(user_login_failed)
        def _on_login_failed(sender, request=None, **kwargs):
            if request is not None:
                record_failed_admin_login(request)

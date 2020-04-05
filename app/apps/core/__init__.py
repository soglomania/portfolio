from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'apps.core'
    label = "core"
    verbose_name = "Core"
    


default_app_config = "apps.core.CoreConfig"
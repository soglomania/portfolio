from django.apps import AppConfig


class UiConfig(AppConfig):
    name = 'apps.ui'
    label = "ui"
    verbose_name = "Ui"

default_app_config = "apps.ui.UiConfig"

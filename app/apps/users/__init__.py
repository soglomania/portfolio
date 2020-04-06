from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'apps.users'
    label = 'users'
    verbose_name = 'Users'


default_app_config = 'apps.users.UsersAppConfig'

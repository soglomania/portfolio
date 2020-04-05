from django.apps import AppConfig


class ResumeConfig(AppConfig):
    name = 'apps.resume'
    label = "resume"
    verbose_name = "Resume"
    

default_app_config = "apps.resume.ResumeConfig"

from django.contrib import admin

from .models import Project
from modeltranslation.admin import TranslationAdmin


class ProjectAdmin(TranslationAdmin):
    pass



admin.site.register(Project, ProjectAdmin)

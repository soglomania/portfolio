from django.contrib import admin

from .models import PersonalInfo
from modeltranslation.admin import TranslationAdmin


class PersonalInfoAdmin(TranslationAdmin):
    pass

admin.site.register(PersonalInfo, PersonalInfoAdmin)

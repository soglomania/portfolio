from django.contrib import admin

from .models import PersonalInfo, Language, Interest
from modeltranslation.admin import TranslationAdmin


class PersonalInfoAdmin(TranslationAdmin):
    pass


class LanguageAdmin(TranslationAdmin):
    pass


class InterestAdmin(TranslationAdmin):
    pass


admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Interest, InterestAdmin)

from django.contrib import admin

from . import models
from modeltranslation.admin import TranslationAdmin


class BiographyAdmin(TranslationAdmin):
    pass

class LanguageAdmin(TranslationAdmin):
    pass

class EducationAdmin(TranslationAdmin):
    pass

class ExperienceAdmin(TranslationAdmin):
    pass

class SkillAdmin(TranslationAdmin):
    pass

class InterestAdmin(TranslationAdmin):
    pass


admin.site.register(models.Biography, BiographyAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Interest, InterestAdmin)

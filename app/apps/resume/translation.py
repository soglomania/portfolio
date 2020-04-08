
from modeltranslation.translator import translator, TranslationOptions
from . import models


class BiographyTranslationOptions(TranslationOptions):
    fields = ('job_title', 'summary', 'description',)


class LanguageTranslationOptions(TranslationOptions):
    fields = ('name', 'level', 'summary', 'description',)


class EducationTranslationOptions(TranslationOptions):
    fields = ('name', 'school', 'summary', 'description',)


class ExperienceTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'description',)


class SkillTranslationOptions(TranslationOptions):
    fields = ('name', 'summary', 'description',)


class InterestTranslationOptions(TranslationOptions):
    fields = ('name', 'summary', 'description',)



translator.register(models.Biography, BiographyTranslationOptions)
translator.register(models.Language, LanguageTranslationOptions)
translator.register(models.Education, EducationTranslationOptions)
translator.register(models.Experience, ExperienceTranslationOptions)
translator.register(models.Skill, SkillTranslationOptions)
translator.register(models.Interest, InterestTranslationOptions)

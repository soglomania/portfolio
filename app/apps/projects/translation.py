
from modeltranslation.translator import translator, TranslationOptions
from .models import Project


class ProjectTranslationOptions(TranslationOptions):
    fields = ('summary', 'description', 'category',)



translator.register(Project, ProjectTranslationOptions)



from modeltranslation.translator import translator, TranslationOptions
from .models import PersonalInfo


class PersonalInfoTranslationOptions(TranslationOptions):
    fields = ('job_title', 'summary',)

translator.register(PersonalInfo, PersonalInfoTranslationOptions)
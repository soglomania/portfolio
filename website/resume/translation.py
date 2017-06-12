
from modeltranslation.translator import translator, TranslationOptions
from .models import PersonalInfo, Language, Interest


class PersonalInfoTranslationOptions(TranslationOptions):
    fields = ('job_title', 'summary',)


class LanguageTranslationOptions(TranslationOptions):
    fields = ('description',)

class InterestTranslationOptions(TranslationOptions):
    fields = ('description',)



translator.register(PersonalInfo, PersonalInfoTranslationOptions)
translator.register(Language, LanguageTranslationOptions)
translator.register(Interest, InterestTranslationOptions)
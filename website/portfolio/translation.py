
from modeltranslation.translator import translator, TranslationOptions
from .models import Project,PersonalInfo, Language, Interest, Membership, Education, Job, Skill


class ProjectTranslationOptions(TranslationOptions):
    fields = ('summary', 'description',)


class PersonalInfoTranslationOptions(TranslationOptions):
    fields = ('job_title', 'summary', 'intro_url')


class LanguageTranslationOptions(TranslationOptions):
    fields = ('description',)

class InterestTranslationOptions(TranslationOptions):
    fields = ('name','level','description',)


class InterestTranslationOptions(TranslationOptions):
    fields = ('name','description',)

class MembershipTranslationOptions(TranslationOptions):
    fields = ('name','description',)


class EducationTranslationOptions(TranslationOptions):
    fields = ('name','summary','description',)


class JobTranslationOptions(TranslationOptions):
    fields = ('title','summary','description',)


class SkillTranslationOptions(TranslationOptions):
    fields = ('name','description',)


translator.register(Project, ProjectTranslationOptions)
translator.register(PersonalInfo, PersonalInfoTranslationOptions)
translator.register(Language, LanguageTranslationOptions)
translator.register(Interest, InterestTranslationOptions)
translator.register(Membership, MembershipTranslationOptions)
translator.register(Education, EducationTranslationOptions)
translator.register(Job, JobTranslationOptions)
translator.register(Skill, SkillTranslationOptions)

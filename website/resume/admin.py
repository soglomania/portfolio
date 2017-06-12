from django.contrib import admin

from .models import PersonalInfo, Language, Interest,Membership, Education, Job, Skill
from modeltranslation.admin import TranslationAdmin


class PersonalInfoAdmin(TranslationAdmin):
    pass


class LanguageAdmin(TranslationAdmin):
    pass


class InterestAdmin(TranslationAdmin):
    pass

class MembershipAdmin(TranslationAdmin):
    pass


class EducationAdmin(TranslationAdmin):
    pass

class JobAdmin(TranslationAdmin):
    pass


class SkillAdmin(TranslationAdmin):
    pass

admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Membership, MembershipAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Skill, SkillAdmin)




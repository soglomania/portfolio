from django.conf.urls import url, include
from django.contrib import admin

from . import views
from portfolio.views import ProjectApiView

urlpatterns = [
    url(r'^$', views.api_swagger, name='api-swagger'),
    url(r'^resume.me/$', views.PersonalInfoView.as_view(), name='resume-me'),
    url(r'^resume.language/$', views.LanguageView.as_view(), name='resume-language'),
    url(r'^resume.interest/$', views.InterestView.as_view(), name='resume-interest'),
    url(r'^resume.education/$', views.EducationView.as_view(), name='resume-education'),
    url(r'^resume.job/$', views.JobView.as_view(), name='resume-job'),
    url(r'^resume.skill/$', views.SkillView.as_view(), name='resume-skill'),
    url(r'^resume.membership/$', views.MembershipView.as_view(), name='resume-membership'),
    url(r'^resume.project/$', ProjectApiView.as_view(), name='resume-project'),


]




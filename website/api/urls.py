from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.api_swagger, name='api-swagger'),
    url(r'^me/$', views.PersonalInfoApiView.as_view(), name='resume-me'),
    url(r'^language/$', views.LanguageApiView.as_view(), name='resume-language'),
    url(r'^interest/$', views.InterestApiView.as_view(), name='resume-interest'),
    url(r'^education/$', views.EducationApiView.as_view(), name='resume-education'),
    url(r'^job/$', views.JobApiView.as_view(), name='resume-job'),
    url(r'^skill/$', views.SkillApiView.as_view(), name='resume-skill'),
    url(r'^membership/$', views.MembershipApiView.as_view(), name='resume-membership'),
    url(r'^project/$', views.ProjectApiView.as_view(), name='resume-project'),
]




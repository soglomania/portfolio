from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.api_swagger, name='api-swagger'),
    url(r'^me/$', views.PersonalInfoApiView.as_view(), name='api-me'),
    url(r'^language/$', views.LanguageApiView.as_view(), name='api-language'),
    url(r'^interest/$', views.InterestApiView.as_view(), name='api-interest'),
    url(r'^education/$', views.EducationApiView.as_view(), name='api-education'),
    url(r'^job/$', views.JobApiView.as_view(), name='api-job'),
    url(r'^skill/$', views.SkillApiView.as_view(), name='api-skill'),
    url(r'^membership/$', views.MembershipApiView.as_view(), name='api-membership'),
    url(r'^project/$', views.ProjectApiView.as_view(), name='api-project'),
]

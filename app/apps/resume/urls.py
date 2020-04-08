from django.conf.urls import url, include

from . import views

app_name = "resume"

urlpatterns = [
    url(r'^resume/?$', views.ResumeApiView.as_view(), name='api-resume'),
    url(r'^resume/biography/?$', views.BiographyApiView.as_view(), name='api-biography'),
    url(r'^resume/languages/?$', views.LanguageApiView.as_view(), name='api-languages'),
    url(r'^resume/educations/?$', views.EducationApiView.as_view(), name='api-educations'),
    url(r'^resume/experiences/?$', views.ExperienceApiView.as_view(), name='api-experiences'),
    url(r'^resume/skills/?$', views.SkillApiView.as_view(), name='api-skills'),
    url(r'^resume/interests/?$', views.InterestApiView.as_view(), name='api-interests'),
]


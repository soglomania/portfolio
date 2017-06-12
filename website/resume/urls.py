from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^about.me/$', views.PersonalInfoView.as_view(), name='about-me'),
    url(r'^about.language/$', views.LanguageView.as_view(), name='about-language'),
    url(r'^about.interest/$', views.InterestView.as_view(), name='about-interest'),
]




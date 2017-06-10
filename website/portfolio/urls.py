from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.ProjectListView.as_view(), name='project-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
]

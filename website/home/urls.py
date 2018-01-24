
from django.conf.urls import url, include
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.index, name='home-index'),
    url(r'^download$', views.download, name='download'),

]

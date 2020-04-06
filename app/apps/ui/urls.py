from django.conf.urls import url, include

from . import views

app_name = "ui"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^portfolio/list/?$', views.Projects.as_view(), name='projects'),
    url(r'^portfolio/(?P<pk>[0-9]+)/?$', views.Project.as_view(), name='project'),
    
    url(r'^french/?$', views.set_french, name='set-french'),
    url(r'^english/?$', views.set_english, name='set-english'),
    url(r'^spanish/?$', views.set_spanish, name='set-spanish'),
]

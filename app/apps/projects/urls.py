from django.conf.urls import url, include

from . import views

app_name = "projects"

urlpatterns = [
    url(r'^projects/?$', views.ProjectApiView.as_view(), name='api-projects'),
]



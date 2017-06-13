from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.post_list, name='blog-post-list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='blog-post-detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='blog-post-edit'),

]
from django.conf.urls import url

from .views import LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView, UserListApiView

app_name = "users"

urlpatterns = [
    url(r'^users/?$', UserListApiView.as_view(), name="users-list"),
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view(), name="users-read-update"),
    url(r'^user/register/?$', RegistrationAPIView.as_view(), name="users-register"),
    url(r'^user/login/?$', LoginAPIView.as_view(), name="users-login"),
]

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api.views import main_view, posts_view

urlpatterns = [
    path('', main_view),
    path('token/', obtain_auth_token),
    path("posts/", posts_view)
]

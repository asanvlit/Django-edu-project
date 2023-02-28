from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, post_add_view

urlpatterns = [
    path("", main_view, name="main"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("posts/add/", post_add_view, name="posts_add")
]

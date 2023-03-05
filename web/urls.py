from django.urls import path

from web.views import main_view, registration_view, auth_view, logout_view, post_edit_view, tags_view, tags_delete_view, \
    post_delete_view, analytics_view, import_view, stat_view, subscriptions_add_view, subscriptions_delete_view, \
    subscriptions_view

urlpatterns = [
    path("", main_view, name="main"),
    path("import/", import_view, name="import"),
    path("analytics/", analytics_view, name="analytics"),
    path("stat/", stat_view, name="stat"),
    path("registration/", registration_view, name="registration"),
    path("auth/", auth_view, name="auth"),
    path("logout/", logout_view, name="logout"),
    path("posts/add/", post_edit_view, name="posts_add"),
    path("posts/<int:id>/", post_edit_view, name="posts_edit"),
    path("posts/<int:id>/delete/", post_delete_view, name="posts_delete"),
    path("subscriptions/", subscriptions_view, name="subscriptions"),
    path("subscriptions/add/", subscriptions_add_view, name="subscriptions_add"),
    path("subscriptions/<int:id>/delete/", subscriptions_delete_view, name="subscriptions_delete"),
    path("tags/", tags_view, name="tags"),
    path("tags/<int:id>/delete", tags_delete_view, name="tags_delete"),
]


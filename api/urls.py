from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from api.views import main_view, PostModelViewSet

router = SimpleRouter()
router.register("posts", PostModelViewSet, basename='posts')

urlpatterns = [
    path('', main_view),
    path('token/', obtain_auth_token),
    *router.urls
]

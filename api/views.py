from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from api.serializers import PostSerializer, TagSerializer
from web.models import Post, PostTag


@api_view(["GET"])
@permission_classes([])
def main_view(request):
    return Response({"status": "ok"})


class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().select_related("user").prefetch_related("tags").filter(user=self.request.user)


class TagsViewSet(ListModelMixin, GenericViewSet):
    serializer_class = TagSerializer

    def get_queryset(self):
        return PostTag.objects.all().filter(user=self.request.user)

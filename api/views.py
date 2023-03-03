from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from api.serializers import PostSerializer
from web.models import Post


@api_view(["GET"])
@permission_classes([])
def main_view(request):
    return Response({"status": "ok"})


@api_view(["GET"])
def posts_view(request):
    posts = Post.objects.all().select_related("user").prefetch_related("tags")
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

from rest_framework import serializers

from web.models import User, PostTag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ('id', 'title')


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    art_type = serializers.CharField()
    hours_spent = serializers.IntegerField()
    used_material = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    user = UserSerializer()
    tags = TagSerializer(many=True)

from rest_framework import serializers

from web.models import User, PostTag, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ('id', 'title')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=PostTag.objects.all(), many=True, write_only=True)

    def save(self, **kwargs):
        tag_ids = self.validated_data.pop("tag_ids")
        self.validated_data['user_id'] = self.context['request'].user.id
        return super().save(**kwargs)

    class Meta:
        model = Post
        fields = ('id', 'art_type', 'hours_spent', 'used_material', 'description', 'tags', 'user', 'tag_ids')

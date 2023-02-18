from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PostTag(models.Model):
    # todo enum for tags
    title = models.CharField(max_length=50)


class Post(models.Model):
    art_type = models.CharField(max_length=50)
    hours_spent = models.IntegerField
    used_material = models.TextField
    description = models.TextField
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(PostTag)
    likes = models.ManyToManyField(User)

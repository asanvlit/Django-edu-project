from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class PostTag(models.Model):
    # todo enum for tags
    title = models.CharField(max_length=50)


class Post(models.Model):
    art_type = models.CharField(max_length=50)
    hours_spent = models.IntegerField()
    used_material = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(PostTag)
    artwork = models.ImageField(upload_to='artworks/', null=True, blank=True)


class Like(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class PostTag(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'тег'


class Post(models.Model):
    art_type = models.CharField(max_length=50, verbose_name='Тип работы')
    hours_spent = models.IntegerField(verbose_name='Потрачено часов')
    used_material = models.TextField(verbose_name='Использованные материалы')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tags = models.ManyToManyField(PostTag, verbose_name='Теги')
    artwork = models.ImageField(upload_to='artworks/', null=True, blank=True, verbose_name='Работа')

    def __str__(self):
        return self.art_type

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Like(models.Model):
    created_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')

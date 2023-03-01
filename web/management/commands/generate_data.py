import random
import string
from random import randint

from django.core.management import BaseCommand

from web.models import User, Post, PostTag


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.first()
        tags = PostTag.objects.filter(user=user)

        posts = []

        for count_index in range(30):
            for post_index in range(randint(5, 10)):
                posts.append(Post(
                    art_type=random.choice(('Цифровая живопись', 'Традиционный рисунок', 'Фотошоп', 'Граффити')),
                    hours_spent=randint(1, 72),
                    used_material=generate_random_string(15),
                    description=generate_random_string(30),
                    user=user,
                ))

        saved_posts = Post.objects.bulk_create(posts)

        post_tags = []
        for post in saved_posts:
            count_of_tags = randint(0, len(tags))
            for tag_index in range(count_of_tags):
                post_tags.append(
                    Post.tags.through(post_id=post.id, posttag_id=tags[tag_index].id)
                )
        Post.tags.through.objects.bulk_create(post_tags)


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

import csv

from web.models import Post, PostTag
from yartone.redis import get_redis_client


def filter_posts(posts_qs, filters):
    if filters['search']:
        posts_qs = posts_qs.filter(art_type__icontains=filters['search'])

    if filters['hours_spent'] is not None:
        if filters['hours_spent']:
            posts_qs = posts_qs.filter(hours_spent__lt=25)
        elif not filters['hours_spent']:
            posts_qs = posts_qs.filter(hours_spent__gt=24)

    if filters['published_at_after']:
        posts_qs = posts_qs.filter(created_at__gte=filters['published_at_after'])

    if filters['published_at_before']:
        posts_qs = posts_qs.filter(created_at__lte=filters['published_at_before'])
    return posts_qs


def export_posts_csv(posts_qs, response):
    writer = csv.writer(response)
    writer.writerow(("art_type", "hours_spent", "used_material", "description", "created_at", "tags"))

    for post in posts_qs:
        writer.writerow((
            post.art_type, post.hours_spent, post.used_material, post.description, post.created_at,
            " ".join([tag.title for tag in post.tags.all()])
        ))
    return response


def import_posts_from_csv(file, user_id):
    strs_from_file = (row.decode() for row in file)
    reader = csv.DictReader(strs_from_file)

    posts = []
    post_tags = []
    for row in reader:
        posts.append(Post(
            art_type=row['art_type'],
            hours_spent=row['hours_spent'],
            used_material=row['used_material'],
            description=row['description'],
            created_at=row['created_at'],
            user_id=user_id
        ))
        post_tags.append(row['tags'].split(" ") if row['tags'] else [])

    tags_map = dict(PostTag.objects.all().values_list("title", "id"))
    saved_posts = Post.objects.bulk_create(posts)
    post_tags = []
    for post, post_tags_item in zip(saved_posts, post_tags):
        for tag in post_tags_item:
            tag_id = tags_map[tag]
            post_tags.append(
                Post.tags.through(post_id=post.id, posttag_id=tag_id)
            )


def get_stat():
    redis = get_redis_client()
    keys = redis.keys("stat_*")
    return [(key.decode().replace("stat_", ''), redis.get(key).decode())
            for key in keys
            ]

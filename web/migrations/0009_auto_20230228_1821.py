# Generated by Django 4.1.5 on 2023-02-28 15:21

from django.db import migrations

from web.models import PostTag


def delete_tags(apps, schema_editor):
    postTags = PostTag.objects.all()
    for tag in postTags:
        tag.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20230228_1701'),
    ]

    operations = [
        migrations.RunPython(delete_tags),
    ]

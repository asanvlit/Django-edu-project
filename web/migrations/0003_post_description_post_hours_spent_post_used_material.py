# Generated by Django 4.1.5 on 2023-02-28 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_post_artwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='')
        ),
        migrations.AddField(
            model_name='post',
            name='hours_spent',
            field=models.IntegerField(default=None)
        ),
        migrations.AddField(
            model_name='post',
            name='used_material',
            field=models.TextField(default='')
        ),
    ]

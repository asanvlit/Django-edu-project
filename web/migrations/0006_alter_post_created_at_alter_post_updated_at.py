# Generated by Django 4.1.5 on 2023-02-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_post_created_at_alter_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
# Generated by Django 5.1.6 on 2025-02-09 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="post_id",
            new_name="post",
        ),
        migrations.RenameField(
            model_name="likedpost",
            old_name="post_id",
            new_name="post",
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("the_blog", "0006_alter_post_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="snippet",
            field=models.CharField(default="Click to read full post", max_length=255),
        ),
    ]
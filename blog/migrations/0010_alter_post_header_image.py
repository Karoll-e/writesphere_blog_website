# Generated by Django 4.2 on 2023-09-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_post_header_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="post_pics"),
        ),
    ]

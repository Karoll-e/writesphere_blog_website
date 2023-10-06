# Generated by Django 4.2 on 2023-10-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_post_resized_header_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="resized_header_image",
        ),
        migrations.AddField(
            model_name="post",
            name="cropped_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="post_images/cropped/"
            ),
        ),
    ]

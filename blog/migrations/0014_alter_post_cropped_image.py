# Generated by Django 4.2 on 2023-10-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0013_remove_post_resized_header_image_post_cropped_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="cropped_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="post_pics/cropped"
            ),
        ),
    ]

# Generated by Django 4.2 on 2023-10-06 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0015_remove_post_cropped_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=200),
        ),
    ]

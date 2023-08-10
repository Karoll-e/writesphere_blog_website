# Generated by Django 4.2 on 2023-08-10 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_rename_category_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="blog.category"
            ),
        ),
    ]

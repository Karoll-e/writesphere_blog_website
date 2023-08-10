# Generated by Django 4.2 on 2023-08-10 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_delete_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=70)),
            ],
        ),
    ]

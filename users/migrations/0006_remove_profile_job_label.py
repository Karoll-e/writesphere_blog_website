# Generated by Django 4.2 on 2023-08-24 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_rename_description_profile_bio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="job_label",
        ),
    ]

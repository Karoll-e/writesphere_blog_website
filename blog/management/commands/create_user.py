import os
import django
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")  # Replace 'your_project' with your project's name
django.setup()

class Command(BaseCommand):
    help = 'Create fake users'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):  # Create 10 users
            first_name = fake.first_name_nonbinary()
            last_name = fake.last_name_nonbinary()
            email = fake.ascii_free_email()
            username = f"{first_name.lower()}{last_name.lower()}" 
            password = 'your_password_here'  # Set the password

            # Create a new user
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

            self.stdout.write(self.style.SUCCESS(f"Created user: {user.username} ({user.email})"))

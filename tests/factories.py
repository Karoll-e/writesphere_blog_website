import factory
from faker import Faker
from django.contrib.auth.models import User
from blog.models import Category, Post

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.user_name()
    email = fake.email()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fake.word()

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker('sentence')
    content = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
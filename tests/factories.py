import factory
from faker import Faker
from django.contrib.auth.models import User
from blog.models import Category, Post

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.user_name()
    email = fake.ascii_free_email()
    password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)

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
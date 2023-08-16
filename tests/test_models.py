import pytest
from django.contrib.auth.models import User
from blog.models import Category, Post
from factories import CategoryFactory, PostFactory, UserFactory

@pytest.mark.django_db
def test_user_creation():
    user = UserFactory()
    print(user.username)
    print(User.objects.count())
    print(User.objects.all().values())

    assert User.objects.count() == 1

@pytest.mark.django_db
def test_post_creation():
    post = PostFactory()
    
    assert Post.objects.count() == 1

@pytest.mark.django_db
def test_category_creation():
    category = CategoryFactory()

    assert Category.objects.count() == 1

@pytest.mark.django_db
def test_post_category_relationship():
    post = PostFactory()

    assert isinstance(post.category, Category)

@pytest.mark.django_db
def test_post_category_relationship_with_category():
    category = CategoryFactory()
    post = PostFactory(category=category)

    assert post.category == category






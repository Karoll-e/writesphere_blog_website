import pytest
from django.contrib.auth.models import User
from blog.models import Category, Post
from factories import CategoryFactory, PostFactory, UserFactory

# Test to ensure that a user can be created using the UserFactory.
@pytest.mark.django_db
def test_user_creation():
    user = UserFactory()
    print(user.username)
    print(User.objects.count())
    print(User.objects.all().values())

    assert User.objects.count() == 1

# Test to ensure that a post can be created using the PostFactory.
@pytest.mark.django_db
def test_post_creation():
    post = PostFactory()
    
    assert Post.objects.count() == 1

# Test to ensure that a category can be created using the CategoryFactory.
@pytest.mark.django_db
def test_category_creation():
    category = CategoryFactory()

    assert Category.objects.count() == 1

# Test to ensure the relationship between a post and its category.
@pytest.mark.django_db
def test_post_category_relationship():
    post = PostFactory()

    assert isinstance(post.category, Category)

# Test to ensure the correct relationship between a post and a specified category.
@pytest.mark.django_db
def test_post_category_relationship_with_category():
    category = CategoryFactory()
    post = PostFactory(category=category)

    assert post.category == category

# Test to ensure the __str__ method of Category and Post models returns the expected string representation.
@pytest.mark.django_db
def test_model_str_representation():
    post = PostFactory()
    category = CategoryFactory()

    assert str(post) == post.title
    assert str(category) == category.name

# Test to ensure the get_absolute_url method of Post model returns the correct URL.
@pytest.mark.django_db
def test_post_get_absolute_url():
    post = PostFactory()

    expected_url = f"/post/{post.id}/"
    actual_url = post.get_absolute_url()

    assert actual_url == expected_url
    


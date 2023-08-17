import pytest
from django.urls import reverse
from django.test import Client
from factories import UserFactory, PostFactory

@pytest.mark.django_db
def test_home_view(client):
    response = client.get(reverse('blog-home'))

    assert response.status_code == 200
    assert 'blog/home.html' in [template.name for template in response.templates]


@pytest.mark.django_db
def test_user_post_list_view(client):
    user = UserFactory()
    username = user.username
    response = client.get(reverse('user-posts', kwargs={'username': username}))

    assert response.status_code == 200
    assert 'blog/user_posts.html' in [template.name for template in response.templates]

@pytest.mark.django_db
def test_post_detail_view(client):
    post = PostFactory()
    
    response = client.get(reverse('post-detail', kwargs={'pk': post.pk}))
    assert response.status_code == 200
    assert 'blog/post_detail.html' in [template.name for template in response.templates]
    assert response.context['post'] == post

# Test to ensures that the post-create view behaves correctly for both unauthenticated and authenticated users.
@pytest.mark.django_db
def test_post_create_view(client):
    user = UserFactory()
    url = reverse('post-create')
    response = client.get(url)
    
    assert response.status_code == 302
    assert response.url == reverse('login') + '?next=' + url

    # Log in the client with the created user.
    client.force_login(user)

    # Simulate a request as a logged-in user.
    response = client.get(url)

    assert response.status_code == 200
    assert 'blog/post_form.html' in [template.name for template in response.templates]


# Test to ensures that the post-update view behaves correctly for both unauthenticated and authenticated users.
@pytest.mark.django_db
def test_post_update_view(client):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory()
        self.other_user = UserFactory(username='otheruser', password='otherpassword')
        self.post = PostFactory()

    def test_view_status_code_and_template(self):
        self.client.login()
        response = self.client.get(reverse('post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        assert 'blog/post_detail.html' in [template.name for template in response.templates]

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('post-update', args=[self.post.pk]))
        print(response.url)
        assert response.url == reverse('login') + '?next=' + reverse('post-update', args=[self.post.pk])

    def test_can_update_own_post(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)

    def test_cannot_update_other_users_post(self):
        self.client.login(username='otheruser', password='otherpassword')
        response = self.client.get(reverse('post-update', args=[self.post.pk]))
        self.assertEqual(response.status_code, 403)  # Expected status code for permission denied

    def test_authenticated_user_can_update_post(self):
        self.client.login(username='testuser', password='testpassword')
        updated_title = 'Updated Title'
        updated_content = 'Updated content for testing'

        response = self.client.post(reverse('post-update', args=[self.post.pk]), {
            'title': updated_title,
            'content': updated_content
        })

        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful update
        updated_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(updated_post.title, updated_title)
        self.assertEqual(updated_post.content, updated_content)
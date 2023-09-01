from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CategoryPostListView
from . import views

urlpatterns = [
    path("", PostListView.as_view(), name='blog-home'),
    path("<str:username>", UserPostListView.as_view(), name='profile'),
    path("post/<int:pk>/", PostDetailView.as_view(), name ='post-detail'),
    path("category/<str:category_name>/", CategoryPostListView.as_view(), name='category_posts'),
    path("post/new/", PostCreateView.as_view(), name ='post-create'),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name ='post-update'),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name ='post-delete'),
    path("about/", views.about, name='blog-about'),
]

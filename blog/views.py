from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Category
from users.models import Profile
from .forms import PostForm
from django.shortcuts import render
from .models import Post

def home(request):

    posts = Post.objects.all().order_by("-date_posted")[:4]
    latest_post = Post.objects.last()

    context = {
        'posts': posts,
        'latest_post': latest_post
    }

    return render(request, 'blog/home.html', context)


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile_user = get_object_or_404(User, username=self.kwargs.get("username"))
        profile = get_object_or_404(Profile, user=profile_user)
        context["profile"] = profile
        return context


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    author = post.author
    author_posts = Post.objects.filter(author=author).order_by("-date_posted")[:4]
    num_posts = author_posts.count()

    context = {"post": post, "author_posts": author_posts, "num_posts": num_posts}
    return render(request, "blog/post_detail.html.", context)


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    redirect_field_name = "next"
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


class CategoryPostListView(ListView):
    model = Post
    template_name = "blog/category_posts.html"  # Create this template
    context_object_name = "posts"
    paginate_by = 5  # Adjust the number of posts per page

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        category = get_object_or_404(Category, name=category_name)
        return Post.objects.filter(category=category).order_by("-date_posted")

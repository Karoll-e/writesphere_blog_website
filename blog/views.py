from typing import Any, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
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
from django.http import JsonResponse
from django.db.models import Count

def home(request):

    posts = Post.objects.all().order_by("-date_posted")[1:5]
    latest_post = Post.objects.last()
    liked_posts = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')[1:5]
    most_popular_post = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes').first()
    context = {
        'posts': posts,
        'latest_post': latest_post,
        'liked_posts': liked_posts,
        'most_popular_post': most_popular_post
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

def like_toggle(model):
    def inner_func(func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('users/login.html')  # Redirect to the login page if the user is not authenticated

            post = get_object_or_404(model, id=kwargs.get('pk'))
            user_exist = post.likes.filter(username=request.user.username).exists()
            
            if user_exist:
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
                    
            return func(request, post)
        return wrapper
    return inner_func


@login_required
@like_toggle(Post)
def like_post(request, post):   
    return render(request, 'snippets/likes.html', {'post' : post })
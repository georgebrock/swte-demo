from django.views.generic import ListView, DetailView

from apps.blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost


class BlogPostDetailView(DetailView):
    model = BlogPost

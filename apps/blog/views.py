from django.views.generic import ListView

from apps.blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost

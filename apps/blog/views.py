from django.views.generic import ListView, DetailView

from apps.blog.models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    queryset = BlogPost.objects.filter(published=True)

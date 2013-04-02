from django.views.generic import ListView, DetailView, CreateView

from apps.blog.models import BlogPost
from apps.blog.forms import BlogPostForm


class BlogPostListView(ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_queryset(self):
        if self.request.GET.get("preview"):
            return BlogPost.objects.all()
        else:
            return BlogPost.objects.filter(published=True)


class BlogPostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPostForm

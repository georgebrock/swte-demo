from django import forms
from django.forms.extras.widgets import SelectDateWidget

from apps.blog.models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ("published", )
        widgets = {
            "publish_date": SelectDateWidget(),
        }

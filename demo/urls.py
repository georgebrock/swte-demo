from django.conf.urls import patterns, include, url
from django.contrib import admin

import apps.blog.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', apps.blog.views.BlogPostListView.as_view(), name='home'),
    url(r'^post/(?P<pk>\d+)/$', apps.blog.views.BlogPostDetailView.as_view(), name='blogpost'),
    url(r'^post/new/$', apps.blog.views.BlogPostCreateView.as_view(), name='new_blogpost'),

    url(r'^admin/', include(admin.site.urls)),
)

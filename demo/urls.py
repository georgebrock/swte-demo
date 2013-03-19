from django.conf.urls import patterns, include, url
from django.contrib import admin

import apps.blog.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', apps.blog.views.BlogPostListView.as_view(), name='home'),

    url(r'^admin/', include(admin.site.urls)),
)

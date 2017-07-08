from django.conf.urls import include, url
from django.contrib import admin
from article.views import *

urlpatterns = (
    url(r'^all/$', articles),
    url(r'^get/(?P<article_id>\d+)/$', article),
)

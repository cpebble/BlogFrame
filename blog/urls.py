from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^page/([\w ]+)', views.page ),
    url(r'^post/([\w ]+)/.*', views.post),
    url(r'^author/([\w ]+)', views.author),
    url(r'^authors/', views.authorlist),
    url(r'^$', views.front, name='front'),
]

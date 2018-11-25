from django.conf.urls import url
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView
)

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url(r'^post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
    url(r'^dev/$', views.dev, name='blog-dev'),
    url(r'^about/', views.about, name='blog-about'),
]
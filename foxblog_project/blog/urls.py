from django.conf.urls import url
from . import views
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='blog-home'),
    url(r'^user/(?P<username>\S+)/$', UserPostListView.as_view(), name='user-posts'),
    url(r'^post/new/', PostCreateView.as_view(), name='post-create'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
    url(r'^dev/$', views.dev, name='blog-dev'),
    url(r'^about/', views.about, name='blog-about'),
]
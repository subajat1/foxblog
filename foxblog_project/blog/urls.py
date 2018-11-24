from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='blog-home'),
    url(r'^dev/$', views.dev, name='blog-dev'),
    url(r'^about/', views.about, name='blog-about'),
]
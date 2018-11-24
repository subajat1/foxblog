from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('subscribe/', views.subscribe_notification, name='blog-subscribe-notif'),
    path('notif_users/', views.notif_users_specific_group, name='blog-notif-users'),
    path('notif_group/', views.notif_group, name='blog-notif-group'),

]
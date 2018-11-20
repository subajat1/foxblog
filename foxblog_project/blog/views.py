from django.shortcuts import render
from django.contrib.auth.models import User
from webpush import send_user_notification, send_group_notification

from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all(),
        'webpush': {'group': 'admin'}
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {'title': 'About!'}
    user = User.objects.get(pk=1)

    return render(request, 'blog/about.html', context)

def notif(request):
    context = {
        'title': 'About!',
        'webpush': {'group': 'admin'}
    }
    user = User.objects.get(pk=1)
    print(user)
    payload = {'head': 'Simple welcome notification', 'body': 'Hello notification using django web-push!!'}
    try:
        ''' send_user_notification still not working '''
        # send_user_notification(user=user, payload=payload, ttl=1000)
        send_group_notification(group_name='admin', payload=payload, ttl=1000)
    except:
        print('push notif failed')

    return render(request, 'blog/notif.html', context)

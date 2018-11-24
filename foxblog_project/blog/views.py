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

    return render(request, 'blog/about.html', context)

def subscribe_notification(request):

    context = {}
    if request.user.is_authenticated:
        group = request.user.groups.all()[0]
        context = {'webpush': {'group': group}}
     
    return render(request, 'blog/subscribe.html', context)

def notif_users_specific_group(request):
    group = 'admin'
    payload_icon = 'https://i.imgur.com/dRDxiCQ.png'
    payload_url = 'http://google.com'
    
    if request.user.is_authenticated:
        print(request.user)

        payload = {"head": "Welcome!", "body": "Hello World"}
        send_user_notification(user=request.user, payload=payload, ttl=1000)

    users = User.objects.filter(groups__name=group)
    print(group)
    if len(users) > 0:
        print(users)
        # for user in users:
        #     payload = {"head": "Welcome!", "body": "Hello World"}
        #     send_user_notification(user=user, payload=payload, ttl=1000)

        # try:
        #     for user in users:
        #         print(user)
        #         payload = { 'head': '[{}] New update!'.format(group), 
        #                     'body': 'Hi {}, you have a new update ...'.format(str(user)),
        #                     'icon': payload_icon,
        #                     'url': payload_url}
        #         payload = {"head": "Welcome!", "body": "Hello World"}
        #         send_user_notification(user=user, payload=payload, ttl=1000)
        # except IndexError:
        #     print('send_user_notification to group: {} is failed.'.format(group))
    else:
        print('no user for group: '.format(group))

    # context = {'users': users, 'group': group}
    context = {}
    return render(request, 'blog/notif_users.html', context)

def notif_group(request):
    group = 'admin'
    
    payload = {"head": "Welcome!", "body": "Hello World"}
    if request.user.is_authenticated:
        send_group_notification(group_name='admin', payload=payload, ttl=1000)
    # send_group_notification(group_name=group, payload=payload, ttl=1000)

    context = {'users': users, 'group': group}
    return render(request, 'blog/notif_group.html')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from .models import Post

def home(request):
    context = {
        'title': 'Fox Blog',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def dev(request):
    return render(request, 'blog/dev.html')

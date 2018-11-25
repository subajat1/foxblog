# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

def home(request):
    context = {
        'title': 'Fox Blog',
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html')

def dev(request):
    return render(request, 'blog/dev.html')

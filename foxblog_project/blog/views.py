# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def dev(request):
    return render(request, 'blog/dev.html')

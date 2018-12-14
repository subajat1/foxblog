# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    fields = ('author', 'title', 'content', 'date_posted',)
    list_display = ('title', 'author', 'date_posted')

from django.apps import AppConfig
from django.db.models.signals import post_save

class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        from .models import Post
        from .signals import notify_new_post
        # post_save.connect(notify_new_post, sender=Post)

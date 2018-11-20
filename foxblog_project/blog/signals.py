from django.db.models import signals
from django.dispatch import receiver
from webpush import send_user_notification, send_group_notification

from .models import Post

@receiver(signals.post_save, sender=Post)
def notify_new_post(sender, **kwargs):
    if kwargs['instance']:
        post = kwargs['instance']
        author = post.author
        post_head = 'New post {}'.format(post.title)
        post_body = '{} on {} \n {}'.format(author.first_name, post.date_posted, post.content)
        payload = { 'head': post_head,
                    'body': post_body,
                    'icon': 'https://i.imgur.com/dRDxiCQ.png',
                    'url': 'https://www.example.com'
                  }
        try:
            send_group_notification(group_name='admin', payload=payload, ttl=1000)
        except:
            print('notif signal is failed.')




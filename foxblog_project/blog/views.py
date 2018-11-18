from django.shortcuts import render

posts = [
    {
        'author': 'muwmuw',
        'title': 'Blog title 1',
        'content': 'lorem ipsum',
        'date_posted': 'August 25, 2018'
    },
    {
        'author': 'wololo',
        'title': 'Blog title 2nd post',
        'content': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum.',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About!'})
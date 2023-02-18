from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Milan KC',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Eliza Shahi',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'January 21, 2022'
    },
]


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)

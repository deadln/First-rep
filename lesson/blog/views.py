from django.shortcuts import render
from django.contrib.auth.models import User
# from django.http import HTTPResponse, HTTPRequest

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'Posts': posts})


def user_posts(request, user):
    #    posts1 = []
    posts = Post.objects.all().filter(author=User.objects.get(username=user))
    #    for post in posts:
    #        if post.author == 'glib':
    #            posts1.append(post)
    return render(request, 'user_posts.html', {'Posts': posts})

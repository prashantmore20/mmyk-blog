from django.shortcuts import render, HttpResponse
from django.urls import path, include
from . import views
from blog.models import Post

# Create your views here.

def blogHome(request):
    allPost = Post.objects.all()
    context = {'allPost' : allPost}
    return render (request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    return render (request, 'blog/blogPost.html')
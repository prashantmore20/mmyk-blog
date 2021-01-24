from django.shortcuts import render, HttpResponse
from django.urls import path, include
from . import views

# Create your views here.

def blogHome(request):
    # return HttpResponse ('This is Blog Home Page')
    return render (request, 'blog/blogHome.html')

def blogPost(request, slug):
    return render (request, 'blog/blogPost.html')
    # return HttpResponse (f'This is Blog Home Page: {slug}')
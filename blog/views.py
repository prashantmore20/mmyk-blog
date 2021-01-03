from django.shortcuts import render, HttpResponse
from django.urls import path, include
from . import views

# Create your views here.

def blogHome(request):
    return HttpResponse ('This is Blog Home Page')

def blogPost(request, slug):
    return HttpResponse (f'This is Blog Home Page: {slug}')
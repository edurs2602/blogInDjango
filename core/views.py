from django.shortcuts import render

from .models import Post, Port

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def port(request):
    ports = Port.objects.all()
    return render(request, 'port.html', {'ports': ports})

def blog(request):
    
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})
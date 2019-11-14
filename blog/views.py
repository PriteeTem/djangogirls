from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .models import Item
from .forms import PostForm
from django.shortcuts import redirect
import plaid
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
_SECRETS_FILE = 'secrets.txt'
_PUBLIC_KEY_ENV = 'PLAID_PUBLIC_KEY'
_CLIENT_ID_ENV = 'PLAID_CLIENT_ID'
_SECRET_ENV = 'PLAID_SECRET'

# Create your views here.
def post_list(request):
    posts= Post.objects.all()
    return render(request, 'blog/post_list.html',{'posts': posts})

def about_page(request):
    return render(request, 'blog/about.html',{})

def team_page(request):
    return render(request, 'blog/team.html',{})

def home_page(request):
    return render(request, 'blog/homepage.html',{})

def plaid_page(request):
    return render(request, 'blog/plaid_page.html',{})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})



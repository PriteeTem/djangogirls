from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
import json
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
from .secrets import Secrets
secrets = Secrets ()

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

def get_access_token(request):
    if request.method != 'POST' :
        return HttpResponse(status= 403)
    print('we are getting the token now')
    print (request.body)
  
    public_token = request.POST["public_token"]
    
    client = plaid.Client(client_id=secrets.client_id, 
                      public_key=secrets.public_key,
                      secret=secrets.secret, 
                      environment='sandbox',
                      suppress_warnings=True)
    response = client.Item.public_token.exchange(public_token)
    print(response)
    access_token = response["access_token"]
    print (access_token)
   
    secrets.access_tokens = secrets.access_tokens + [access_token]
    try:
        auth_response = client.Auth.get(access_token)
        print("We did it")
        print(auth_response)
        return HttpResponse()
    except plaid.errors.PlaidError as e:
        print(e)
        return HttpResponse(status= 403)
        # return jsonify({'error': {'display_message': e.display_message, 'error_code': e.code, 'error_type': e.type } })
        # print(auth_response)
        # return jsonify({'error': None, 'auth': auth_response})
        
    # Retrieve ACH or EFT account numbers for an Item
    # https://plaid.com/docs/#auth
    

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



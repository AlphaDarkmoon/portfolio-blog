from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import *

from django.db.models import Q
from django.core.paginator import Paginator

from .models import Comment,Post


def github(request):
    return render(request,"github.html",{
        'posts':Post.objects.filter(user_id=request.user.id).order_by("id").reverse(),
        'top_posts':Post.objects.all().order_by("-likes"),
        'recent_posts':Post.objects.all().order_by("-id"),
        'user':request.user,
        'media_url':settings.MEDIA_URL
    })


def search(request):
    query = request.GET.get('q', '').strip()  # Get query from GET request
    
    if not query:  # Handle cases where query is None or empty
        return render(request, "search.html", {
            'query': None,
            'page_obj': None,
            'media_url': settings.MEDIA_URL,
            'error': "Please enter a search term."
        })
    
    # Filter posts based on the query
    results = Post.objects.filter(
        Q(postname__icontains=query) | Q(category__icontains=query)
    ).order_by("-id")

    paginator = Paginator(results, 6)
    page_number = request.GET.get('page')  # Get current page number
    page_obj = paginator.get_page(page_number)
    
    # Render the results page
    return render(request, "search.html", {
        'query': query,
        'page_obj': page_obj,
        'media_url': settings.MEDIA_URL,
    })

def all_posts(request):
    posts = Post.objects.all().order_by('-id')  # Get all posts
    
    paginator = Paginator(posts, 6)  # Paginator to display 6 posts per page
    page_number = request.GET.get('page')  # Get current page number
    page_obj = paginator.get_page(page_number)

    # Render the all posts page
    return render(request, "posts.html", {
        'page_obj': page_obj,
        'media_url': settings.MEDIA_URL,
    })

def blog(request):
    return render(request,"blog.html",{
            'posts':Post.objects.filter(user_id=request.user.id).order_by("id").reverse(),
            'top_posts':Post.objects.all().order_by("-likes"),
            'recent_posts':Post.objects.all().order_by("-id"),
            'user':request.user,
            'media_url':settings.MEDIA_URL
        })
    
    


def post(request,id):
    post = Post.objects.get(id=id)
    
    return render(request,"git-posts.html",{
        "user":request.user,
        'post':Post.objects.get(id=id),
        'recent_posts':Post.objects.all().order_by("-id"),
        'media_url':settings.MEDIA_URL,
        'comments':Comment.objects.filter(post_id = post.id),
        'total_comments': len(Comment.objects.filter(post_id = post.id))
    })
    
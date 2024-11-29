from django.shortcuts import render,redirect, get_object_or_404
from django.conf import settings
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Comment,Post
from .forms import NewsletterSubscriptionForm
from django.shortcuts import render, redirect
from .forms import NewsletterSubscriptionForm

def blogsHome(request):
    # Handle form submission
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()  # Save the email to the database
            return redirect('blogs:confirmation')  # Redirect to the confirmation page after saving
    else:
        form = NewsletterSubscriptionForm()

    # Return the main page with the form
    return render(request, "blogs/blogs-Home.html", {
        'posts': Post.objects.filter(user_id=request.user.id).order_by("id").reverse(), # Show posts in reverse order (latest to older posts)
        'top_posts': Post.objects.all().order_by("-likes"),
        'recent_posts': Post.objects.all().order_by("-id"),
        'user': request.user,
        'media_url': settings.MEDIA_URL,
        'form': form
    })



def searchResult(request):
    query = request.GET.get('q', '').strip() # Get querry from Search bar
    if not query:  # Handle cases where query is None or empty
        return render(request, "blogs/search-Result.html", {
            'query': None,
            'page_obj': None,
            'media_url': settings.MEDIA_URL,
            'error': "Please enter a search term."
        })
    
    # Filter posts based on the query
    results = Post.objects.filter(
        Q(postname__icontains=query) | Q(category__icontains=query)
    ).order_by("-id")

    paginator = Paginator(results, 6) # Show only 6 posts per page
    page_number = request.GET.get('page')  # Get current page number
    page_obj = paginator.get_page(page_number)
    
    # Render the results page
    return render(request, "blogs/search-Result.html", {
        'query': query,
        'page_obj': page_obj,
        'media_url': settings.MEDIA_URL,
    })

def postList(request):
    posts = Post.objects.all().order_by('-id')  # Get all posts
    paginator = Paginator(posts, 6)  # Paginator to display 6 posts per page
    page_number = request.GET.get('page')  # Get current page number
    page_obj = paginator.get_page(page_number)

    # Render the all posts page
    return render(request, "blogs/posts-List.html", {
        'page_obj': page_obj,
        'media_url': settings.MEDIA_URL,
    })  

def postExpend(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    return render(request, "blogs/post-Expend.html", {
        "user": request.user,
        "post": post,
        "recent_posts": Post.objects.all().order_by("-id"),
        "media_url": settings.MEDIA_URL
    })
    
def confirmation(request):
    return render(request, "blogs/newslatter-Confirmation.html")


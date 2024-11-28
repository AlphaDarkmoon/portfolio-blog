from . import views
from django.urls import path

app_name = 'blogs'

urlpatterns = [
    path("",views.github,name="blogs-home"),
    path("post/<slug:slug>/",views.post,name="post"),
    path('search/', views.search, name='search'),
    path('posts/', views.all_posts, name='posts'),
    path("confirmation/", views.confirmation, name="confirmation"),
]

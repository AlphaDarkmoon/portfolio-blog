from . import views
from django.urls import path, include

app_name = 'blogs'

urlpatterns = [
    path("",views.blogsHome,name="blogs-home"),
    path("post/<slug:slug>/",views.postExpend,name="post"),
    path('search/', views.searchResult, name='search'),
    path('posts/', views.postList, name='posts'),
    path("confirmation/", views.confirmation, name="confirmation"),
    path('tinymce/', include('tinymce.urls')),
]

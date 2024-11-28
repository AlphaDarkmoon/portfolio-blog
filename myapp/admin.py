from django.contrib import admin
from .models import Post,Comment,Contact
# Register your models here.

# admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)

from .models import Post

admin.site.site_header = 'BLOGSPOT | ADMIN PANEL'
admin.site.site_title = 'BLOGSPOT | BLOGGING WEBSITE'
admin.site.index_title= 'BlogSpot Site Administration'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('postname', 'category', 'time', 'likes', 'user')
    search_fields = ('postname', 'category', 'content')
    list_filter = ('category', 'time', 'user')

from django.contrib import admin
from .models import NewsletterSubscription

class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')  # Columns to display in the admin list view
    search_fields = ('email',)  # Allow searching by email address
    list_filter = ('subscribed_at',)  # Filter by subscription date
    ordering = ('-subscribed_at',)  # Order by subscription date, newest first

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)

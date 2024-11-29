from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import Post, Comment, Contact, NewsletterSubscription

# Register Comment and Contact models
admin.site.register(Comment)
admin.site.register(Contact)

# Customize Admin Panel Headers
admin.site.site_header = 'BLOGSPOT | ADMIN PANEL'
admin.site.site_title = 'BLOGSPOT | BLOGGING WEBSITE'
admin.site.index_title = 'BlogSpot Site Administration'

# Customize Post Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('postname', 'category', 'time', 'likes', 'user')
    search_fields = ('postname', 'category', 'content')
    list_filter = ('category', 'time', 'user')

    # Use TinyMCE for the 'content' field
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

# Customize NewsletterSubscription Admin
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',) 
    list_filter = ('subscribed_at',)
    ordering = ('-subscribed_at',)

admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)

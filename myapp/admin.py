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
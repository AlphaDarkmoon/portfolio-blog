from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  
from ckeditor.fields import RichTextField
from django.utils.text import slugify

now =  datetime.now()
time = now.strftime("%d %B %Y")
# Create your models here.

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Post(models.Model):
    postname = models.CharField(max_length=600, db_index=True)
    category = models.CharField(max_length=600, db_index=True)
    image = models.ImageField(upload_to='images/posts', blank=True, null=True, db_index=True)
    # Define a thumbnail using ImageSpecField
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(400, 212)],  # Resize to 400x212 and crop to fit
        format='JPEG',
        options={'quality': 100},  # Optimize quality
    )

    content = RichTextField()
    time = models.CharField(default=time, max_length=100, blank=True, db_index=True)
    likes = models.IntegerField(null=True, blank=True, default=0, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    slug = models.SlugField(unique=True, blank=True, max_length=100, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.postname)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.postname)
    
    
class Comment(models.Model):
    content = models.CharField(max_length=200)
    time = models.CharField(default=time,max_length=100, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return  f"{self.id}.{self.content[:20]}..."
    
    

class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000, blank=True)

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
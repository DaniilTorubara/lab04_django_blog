from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
#pip install django-ckeditor
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null = True, blank = True, upload_to = 'images/profiles/')
    vk_url = models.CharField(max_length = 255, blank = True, null = True)
    instagram_url = models.CharField(max_length = 255, blank = True, null = True)
    twitter_url = models.CharField(max_length = 255, blank = True, null = True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextField(blank = True, null = True)
    image = models.ImageField(null = True, blank = True, upload_to = 'images/')
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length = 255, default = 'uncategorized')
    snippet = models.CharField(max_length = 255, default = 'Click to read full post')
    likes = models.ManyToManyField(User, related_name = 'blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse('home')


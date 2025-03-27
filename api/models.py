from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import render


class Image(models.Model):
    key = models.CharField(max_length=100, help_text="The public id of the uploaded file")
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100, help_text='The original name of the uploaded image')
    created_at = models.DateTimeField(auto_now_add=True)
    
def upload_media(request):
    return render(request, 'upload_media.html')

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField(max_length=200, blank=True, null=True)
    image_link = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True)

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('trilogy', 'Trilogy'),
        ('sequel', 'Sequel'),
        ('standalone', 'Standalone'),
        ('series', 'Series'),
    ]
    
    title = models.CharField(max_length=255)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    video_url = models.URLField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    genre = models.JSONField(default=list) # Store genres as an array
    cast = models.JSONField(default=list) # Store cast as an array
    director = models.CharField(max_length=255, blank=True, null=True)
    series = models.CharField(max_length=255) # For grouping
    order = models.IntegerField() # Order within the series
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title


class Collection(models.Model):
    TYPE_CHOICES = [
        ('trilogy', 'Trilogy'),
        ('sequel', 'Sequel'),
        ('standalone', 'Standalone'),
        ('series', 'Series'),
    ]

    title = models.CharField(max_length=255)
    movies = models.ManyToManyField(Movie)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    order = models.IntegerField()


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return f"{self.user.username}'s Watchlist"
    
class MainPage(models.Model):
    movies = models.ManyToManyField(Movie)
    collection = models.ManyToManyField(Collection)
    

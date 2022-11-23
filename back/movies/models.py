from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.TextField()
    original_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=100)
    vote_average = models.FloatField(default=0)
    vote_count = models.IntegerField(default=0)
    popularity = models.FloatField(default=0)
    adult = models.BooleanField(default=False)
    view_cnt = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre, related_name='genre_movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    related_movies = models.ManyToManyField("self", blank=True)
    wavve = models.CharField(max_length=100)
    watcha = models.CharField(max_length=100)
    netfilx = models.CharField(max_length=100)
    disney_plus = models.CharField(max_length=100)
    amazon_prime_video = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
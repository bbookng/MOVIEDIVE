from django.db import models
from django.conf import settings
from datetime import datetime, timedelta, timezone
from movies.models import Movie

# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
    rate = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return self.created_at.date

    def __str__(self):
        return self.content

class Comment(models.Model):
    Review = models.ForeignKey(Review, related_name="comments", on_delete= models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def created_string(self):
            time = datetime.now(tz=timezone.utc) - self.created_at
            if time < timedelta(minutes=1):
                return '방금 전'
            elif time < timedelta(hours=1):
                return str(int(time.seconds / 60)) + '분 전'
            elif time < timedelta(days=1):
                return str(int(time.seconds / 3600)) + '시간 전'
            elif time < timedelta(days=7):
                time = datetime.now(tz=timezone.utc).date() - self.registered_date.date()
                return str(time.days) + '일 전'
            else:
                return self.created_at.date
    def __self__(self):
        return self.content
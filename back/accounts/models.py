from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(max_length=10)
    profile_img = models.ImageField(blank=True)
    message = models.CharField(max_length=20)
from django.db import models

# Create your models here.

class ActorQuiz(models.Model):
    actor_img = models.ImageField(blank=True)
    answer = models.CharField(max_length=20)

class OXQuiz(models.Model):
    question = models.TextField()
    answer = models.BooleanField()

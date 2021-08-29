from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    img = models.URLField(max_length=200)
    summary = models.TextField()

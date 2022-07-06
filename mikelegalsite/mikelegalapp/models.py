from django.db import models

# Create your models here.

class Movie_List(models.Model):
    Title = models.CharField(max_length=100)
    Release_Date = models.DateField()
    Genre = models.CharField(max_length=100)
    Price = models.IntegerField()
    Rating = models.IntegerField()


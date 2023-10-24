from django.db import models
from datetime import time

class Showtimes (models.Model):
  showtime = models.TimeField()
  def __str__(self):
    return self.showtime.strftime('%H:%M')


# Create your models here.
class Movie (models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  #Each showtime can have multiple movies, each movie can have multiple showtimes
  showtime = models.ManyToManyField(Showtimes)
  
  def __str__(self):
    return self.title

class Customer (models.Model):
  name = models.CharField(max_length=200)
  #Each customer is able to see one movie. Movies can have many customers
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  seatNumber = models.IntegerField()
  
  def __str__(self):
    return self.name

#General Movie Database Model (Showtimes are added after saving the entry):
#movie1 = Movie(title="Ponyo", description="A goldfish princess who meets a human boy slowly becomes human each day that boy is her friend.")

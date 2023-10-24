from rest_framework import serializers
from .models import Movie, Customer, Showtimes
  
class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'title', 'description', 'showtime')
  
class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ('id', 'name', 'movie', 'seatNumber')
  
class ShowtimesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Showtimes
    fields = ('id', 'showtime')
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APITestCase
from movies.models import Movie, Customer, Showtimes
from datetime import time
from django.urls import reverse

# Create your tests here.
class MoviesTestCase(TestCase):
    def setUp(self):
      movie = Movie.objects.create(title="My Neighbor Totoro", description=" the movie ollows schoolgirl Satsuke and her younger sister, Mei, as they settle into an old country house with their father and wait for their mother to recover from an illness in an area hospital.")
      showtime1 = Showtimes.objects.create(showtime=time(hour=10, minute=0))
      movie.showtime.add(showtime1)
      

    def test_movie_creation(self):
      movie = Movie.objects.get(title="My Neighbor Totoro")
      self.assertEqual(movie.title, "My Neighbor Totoro")

    def test_showtimes(self):
      movie = Movie.objects.get(title="My Neighbor Totoro")
      showtimes = Showtimes.objects.get(showtime=time(hour=10, minute=0))
      self.assertEqual(movie.showtime.get(pk=1), showtimes)

    def test_customer_creation(self):
      customer = Customer.objects.create(name="Tsukasa", movie=Movie.objects.get(title="My Neighbor Totoro"), seatNumber="32")
      self.assertEqual(customer.name, "Tsukasa")

class EndpointsTestCase(TestCase):
  def setUp(self):
    self.client = Client()

  def test_get(self):
    response = self.client.get(reverse("movies:index"))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_post(self):
    movie = Movie.objects.create(title="My Neighbor Totoro", description=" the movie ollows schoolgirl Satsuke and her younger sister, Mei, as they settle into an old country house with their father and wait for their mother to recover from an illness in an area hospital.")
    response = self.client.post(reverse("movies:index"), data={"name": "Tsukasa", "movie": movie.id, "seatNumber": "32"})
    self.assertEqual(response.status_code, status.HTTP_200_OK)
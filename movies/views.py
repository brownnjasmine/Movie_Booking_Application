from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views import View
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Movie, Customer, Showtimes

#Test view because i don't know what i'm doing?
def index(request):
    return HttpResponse("Hello, world.")

#Renders the list of movies using serialized data
def ListMovies(request):
    movies = Movie.objects.all()

    
    serialized_data = [{
      'id' : movie.id,
      'title' : movie.title,
      'showtimes' : list(movie.showtime.all().values())
    } for movie in movies
    ]
  
    #response_data = {
     # 'count' : len(serialized_data),
      #'results' : serialized_data,
    #}
    template = loader.get_template("movies/index.html")
    context = {"serialized_data" : serialized_data}
    return HttpResponse(template.render(context, request))

#Returns data about a singular movie
def MovieDetail(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  serialized_data = [{
    'id' : movie.id,
    'title' : movie.title,
    'description' : movie.description,
    'showtimes' : list(movie.showtime.all().values())
  }]

  template = loader.get_template("movies/details.html")
  context = {"serialized_data" : serialized_data}
  return HttpResponse(template.render(context, request))


def BookTicket(request):
  
  if request.method == "POST":
    movie_selection =  get_object_or_404(Movie, pk=request.POST.get("movie"))
    customer = Customer.objects.create(
      name = request.POST.get("name"),
      movie = movie_selection,
      seatNumber = request.POST.get("seatNumber")
    )
    customer.save()
    return HttpResponseRedirect(reverse("movies:index"))
  else:
    movies = Movie.objects.all()
    serialized_data = [{
      'id' : movie.id,
      'title' : movie.title,
    } for movie in movies
    ]
    template = loader.get_template("movies/bookticket.html")
    context = {"serialized_data" : serialized_data}
    return HttpResponse(template.render(context, request))
 

def ViewBookings(request, movie_id):
  movie = get_object_or_404(Movie, pk=movie_id)
  customers = get_list_or_404(Customer, movie=movie)
  #Customer.objects.filter(movie=movie)
  
  template = loader.get_template("movies/bookings.html")
  context = {"customers" : customers, "movie" : movie}
  return HttpResponse(template.render(context, request))
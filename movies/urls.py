from django.urls import path

from . import views

app_name = "movies"
urlpatterns = [
    path("", views.ListMovies, name="index"),
    path("<int:movie_id>/", views.MovieDetail, name="details"),
    path("bookticket/", views.BookTicket, name="bookticket"),
    path("<int:movie_id>/bookings", views.ViewBookings, name="bookings"),
]
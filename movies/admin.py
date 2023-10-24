from django.contrib import admin
from .models import Movie, Showtimes, Customer
# Register your models here.
admin.site.register(Movie)

admin.site.register(Showtimes)

admin.site.register(Customer)
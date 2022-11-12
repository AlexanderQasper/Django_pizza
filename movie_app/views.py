from django.shortcuts import render
from .models import Movies


# Create your views here.

def show_all_movie(request):
    movies = Movies.objects.all()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })

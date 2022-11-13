from django.shortcuts import render
from .models import Movies


# Create your views here.

def show_all_movie(request):
    movies = Movies.objects.all()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })


def show_one_movie(request, id_movie: int):
    movie = Movies.objects.get(id=id_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

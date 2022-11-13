from django.shortcuts import render, get_object_or_404
from .models import Movies


# Create your views here.

def show_all_movie(request):
    movies = Movies.objects.all()
    # for movie in movies:
    #     movie.save() - для слэга всей базы имён во время вызова
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })


def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movies, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

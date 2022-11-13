from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movies


# Create your views here.

def show_all_movie(request):
    #movies = Movies.objects.order_by(F('name').desc(nulls_last=True), 'rating')
    movies = Movies.objects.annotate(
        true_bool = Value(True),
        false_bool = Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget')+1000,
        rand_field=F('budget')+F('year')
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Max('year'), Min('year'))
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'agg' : agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movies, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })

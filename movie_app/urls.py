from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('movie_app.urls')),
    path('movie/<int: id_movie>', views.show_one_movie, name='movie-detail'),
]

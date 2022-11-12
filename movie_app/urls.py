from django.contrib import admin
from django.urls import path, include
from horoscope import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls')),
]
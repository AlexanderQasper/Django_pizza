from django.urls import path, include
from . import views

urlpatterns = [
    path('leo/', views.leo),
    path('taurus/', views.taurus),
    path('gemini/', views.gemini),
    path('cancer/', views.cancer),
]
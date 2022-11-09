from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('<int:zodiac_sign>/', views.get_zodiac_number_info),
    path('<str:zodiac_sign>/', views.get_zodiac_info, name = 'horoscope-name')
]

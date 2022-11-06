from django.urls import path, include
from . import views

urlpatterns = [
    path('<zodiac_sign>/', views.get_zodiac_info),
]
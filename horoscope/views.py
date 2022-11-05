from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def leo(request):
    return HttpResponse('Знак зодиака - ЛЕВ!')

def aries(request):
    return HttpResponse('Овен (Aries) 21 марта – 20 апреля')

def taurus(request):
    return HttpResponse('Телец (Taurus) 21 апреля – 20 мая')

def gemini(request):
    return HttpResponse('Близнецы (Gemini) 21 мая – 21 июня')

def cancer(request):
    return HttpResponse('Рак (Cancer) 22 июня – 22 июля')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def get_zodiac_info(request, zodiac_sign):
    if zodiac_sign == 'leo':
        return HttpResponse('Знак зодиака - ЛЕВ!')
    elif zodiac_sign == 'aries':
        return HttpResponse('Овен (Aries) 21 марта – 20 апреля')
    elif zodiac_sign == 'taurus':
        return HttpResponse('Телец (Taurus) 21 апреля – 20 мая')
    elif zodiac_sign == 'gemini':
        return HttpResponse('Близнецы (Gemini) 21 мая – 21 июня')
    elif zodiac_sign == 'cancer':
        return HttpResponse('Рак (Cancer) 22 июня – 22 июля')
    else:
        return HttpResponseNotFound(f'Не найдена команда {zodiac_sign}')


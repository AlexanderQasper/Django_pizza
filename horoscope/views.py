from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

dict_zodiac = {
    'leo': 'Знак зодиака - ЛЕВ!',
    'aries': 'Овен (Aries) 21 марта – 20 апреля',
    'taurus': 'Телец (Taurus) 21 апреля – 20 мая',
    'gemini': 'Близнецы (Gemini) 21 мая – 21 июня',
    'cancer': 'Рак (Cancer) 22 июня – 22 июля'
}


def get_zodiac_info(request, zodiac_sign):
    description = dict_zodiac.get(zodiac_sign, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Не найдена команда {zodiac_sign}')

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

dict_zodiac = {
    'leo': 'Знак зодиака - ЛЕВ!',
    'aries': 'Овен (Aries) 21 марта – 20 апреля',
    'taurus': 'Телец (Taurus) 21 апреля – 20 мая',
    'gemini': 'Близнецы (Gemini) 21 мая – 21 июня',
    'cancer': 'Рак (Cancer) 22 июня – 22 июля'
}


def get_zodiac_info(request, zodiac_sign: str):
    description = dict_zodiac.get(zodiac_sign, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Не найдена команда {zodiac_sign}')


def get_zodiac_number_info(request, zodiac_sign: int):
    zodiacs = list(dict_zodiac)
    if zodiac_sign > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный номер знака зодиака')
    name_zodiac = zodiacs[zodiac_sign - 1]
    return HttpResponseRedirect(f'/horoscope/{name_zodiac}')

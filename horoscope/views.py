from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from dataclasses import dataclass

dict_zodiac = {
    'leo': 'Знак зодиака - ЛЕВ!',
    'aries': 'Овен (Aries) 21 марта – 20 апреля',
    'taurus': 'Телец (Taurus) 21 апреля – 20 мая',
    'gemini': 'Близнецы (Gemini) 21 мая – 21 июня',
    'cancer': 'Рак (Cancer) 22 июня – 22 июля'
}


def index(request):
    zodiacs = list(dict_zodiac)
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)


@dataclass
class Person:
    name: str
    age: int

    def __str__(self):
        return f'This is {self.name}'


def get_zodiac_info(request, zodiac_sign: str):
    description = dict_zodiac.get(zodiac_sign)
    data = {
        'description_zodiac': description,
        'sign': zodiac_sign.title(),
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_zodiac_number_info(request, zodiac_sign: int):
    zodiacs = list(dict_zodiac)
    if zodiac_sign > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный номер знака зодиака')
    name_zodiac = zodiacs[zodiac_sign - 1]
    redirect_url = reverse('horoscope-name', args=('name_zodiac',))
    return HttpResponseRedirect(redirect_url)

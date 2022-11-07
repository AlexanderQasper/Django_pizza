from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


dict_zodiac = {
    'leo': 'Знак зодиака - ЛЕВ!',
    'aries': 'Овен (Aries) 21 марта – 20 апреля',
    'taurus': 'Телец (Taurus) 21 апреля – 20 мая',
    'gemini': 'Близнецы (Gemini) 21 мая – 21 июня',
    'cancer': 'Рак (Cancer) 22 июня – 22 июля'
}


def index(request):
    zodiacs = list(dict_zodiac)
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()}</a> </li>"
    response = f'''
    <ul>
        <h2> {li_elements} </h2>
    </ul>
    '''
    return HttpResponse(response)


def get_zodiac_info(request, zodiac_sign: str):
    descrption = dict_zodiac.get(zodiac_sign)
    data = {
        'description_zodiac': descrption,
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_zodiac_number_info(request, zodiac_sign: int):
    zodiacs = list(dict_zodiac)
    if zodiac_sign > len(zodiacs):
        return HttpResponseNotFound(f'Неправильный номер знака зодиака')
    name_zodiac = zodiacs[zodiac_sign - 1]
    redirect_url = reverse('horoscope-name', args=('name_zodiac',))
    return HttpResponseRedirect(redirect_url)

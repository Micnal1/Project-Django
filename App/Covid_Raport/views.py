from django.shortcuts import render
from .api_client import get_raport, get_country_raport, search_country
from datetime import date


# Create your views here.
def index(request):
    pass


def Home_covid(request):
    country_list = search_country()

    data = {'data': country_list}

    return render(request, 'home.html', data)


def Country_detalis(request,country):
    time = date.today()
    raport = get_raport(country, time)

    data = {'data': raport, 'number': raport}

    return render(request, 'country_detalis.html', data)

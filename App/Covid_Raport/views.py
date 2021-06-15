from django.shortcuts import render
from .api_client import get_raport, get_country_raport
from datetime import date

# Create your views here.
def index(request):
    pass

def Home_covid(request):

    time = date.today()
    raport = get_raport('poland',time)
    #raport = get_country_raport()


    data ={'data':raport,'number':raport}

    return render(request,'country_detalis.html',data)


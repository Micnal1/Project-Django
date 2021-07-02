from django.shortcuts import render
from .api_client import get_raport, search_country
from datetime import date
from .forms import SearchForm
from .diagrams import b,c


# Create your views here.
def index(request):
    pass


def Home_covid(request):
    country_list = search_country()
    form = SearchForm
    data = {'data': country_list, 'form':form}
    if request.method == "POST":
        if form.is_valid:
            form_data = form(request.POST).data.dict().pop('query')
            print(form_data)
            print(str(form))
            data = {'data':search_country(form_data), 'form':form}
            return render(request, 'result.html', data)

    return render(request, 'home.html', data)


def Country_detalis(request,country):
    time = date.today()
    raport = get_raport(country, time)
    form = SearchForm

    diagram = b

    #print(diagram)


    data = {'data': raport, 'number': raport,'form':form, "diagram":diagram}

    return render(request, 'country_detalis.html', data)




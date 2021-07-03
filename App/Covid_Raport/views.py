from django.shortcuts import render
from .api_client import get_raport, search_country , data_for_diagram
from .forms import SearchForm
from .diagrams import get_diagram


# Create your views here.
def index(request):
    pass


def Home_covid(request):
    country_list = search_country()
    form = SearchForm
    data = {'data': country_list, 'form': form}
    if request.method == "POST":
        if form.is_valid:
            form_data = form(request.POST).data.dict().pop('query')
            data = {'data': search_country(form_data), 'form': form}
            return render(request, 'result.html', data)

    return render(request, 'home.html', data)


def Country_detalis(request, country):
    raport = get_raport(country)
    form = SearchForm

    diagram_data = data_for_diagram(country,3)
    print(diagram_data)
    diagram = get_diagram(data_for_diagram(country,30))
    #diagram = None

    data = {'data': raport, 'number': raport, 'form': form, "diagram": diagram}

    return render(request, 'country_detalis.html', data)

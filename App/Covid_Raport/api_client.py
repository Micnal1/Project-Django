import requests
from datetime import date, timedelta


def get_heders_and_response(endpoint, querystring=None):
    url = f"https://covid-193.p.rapidapi.com/{endpoint}"

    headers = {
        'x-rapidapi-key': "af83ac33ccmsh0117c1c8e6f5d8fp1e3768jsn91b522d919de",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()["response"]


def search_country(country=None):
    endpoint = "countries"

    if country:
        querystring = {"search": country}
        response = get_heders_and_response(endpoint, querystring)

    else:
        response = get_heders_and_response(endpoint)

    return response


def get_raport(country, day=date.today()):
    endpoint = "history"
    querystring = {"country": country, "day": day}

    response = get_heders_and_response(endpoint, querystring)
    return response


def data_for_diagram(country, number_last_days):
    data = {'time': [], 'active': [], 'total': [], 'deaths': []}
    for i in range(number_last_days, 0, -1):
        try:
            time = date.today() - timedelta(days=i)
            data['time'].append(time)
            data_filter = get_raport(country, day=time)[0]
            data['active'].append(data_filter['cases']['active'])
            data['total'].append(data_filter['cases']['total'])
            data['deaths'].append(data_filter['deaths']['total'])
        except:
            data['time'].pop()


    return data

import requests


def search_country(country=False):
    url = "https://covid-193.p.rapidapi.com/countries"

    headers = {
        'x-rapidapi-key': "af83ac33ccmsh0117c1c8e6f5d8fp1e3768jsn91b522d919de",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    if country:
        querystring = {"search": country}
        response = requests.request("GET", url, headers=headers, querystring=querystring)

    else:
        response = requests.request("GET", url, headers=headers)

    return response.json()["response"]


def get_raport(country, day):
    url = "https://covid-193.p.rapidapi.com/history"

    querystring = {"country": country, "day": day}

    headers = {
        'x-rapidapi-key': "af83ac33ccmsh0117c1c8e6f5d8fp1e3768jsn91b522d919de",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()["response"]


def get_country_raport():
    url = "https://covid-193.p.rapidapi.com/countries"

    querystring = {"search": "Poland"}

    headers = {
        'x-rapidapi-key': "af83ac33ccmsh0117c1c8e6f5d8fp1e3768jsn91b522d919de",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()

import requests


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


def get_raport(country, day):
    endpoint = "history"
    querystring = {"country": country, "day": day}

    response = get_heders_and_response(endpoint, querystring)
    return response

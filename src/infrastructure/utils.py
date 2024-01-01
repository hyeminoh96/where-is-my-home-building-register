import requests


def get_request(url, params):
    response = requests.get(url, params=params)
    return response



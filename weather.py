from typing import List

import requests


def get_weather(location: str):
    url = 'https://wttr.in/{location}'.format(location=location)
    queries = {'nTqm': '',
               'lang': 'ru'}
    response = requests.get(url, params=queries)
    response.raise_for_status()

    print(response.text)


def get_weathers(locations: List[str]):
    for location in locations:
        get_weather(location)


if __name__ == '__main__':
    get_weathers(['Лондон', 'Шереметьево', 'Череповец'])

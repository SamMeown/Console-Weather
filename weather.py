import requests


def get_weather(location: str) -> str:
    url = 'https://wttr.in/{location}'.format(location=location)
    queries = {'nTqm': '',
               'lang': 'ru'}
    response = requests.get(url, params=queries)
    response.raise_for_status()

    return response.text


if __name__ == '__main__':
    places = ['Лондон', 'Шереметьево', 'Череповец']
    for place in places:
        print(get_weather(place))

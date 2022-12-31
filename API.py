import requests


def get_fact():
    r = requests.get('https://api.chucknorris.io/jokes/random')

    if r.status_code == 200:
        res = r.json()
        return res['value']

    return 'The only time we fail is when we stop trying'

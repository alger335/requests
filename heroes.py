import requests

TOKEN = "2619421814940190"


def get_heroes(heroes_list):
    hero_int = {}
    for hero in heroes_list:
        url = f"https://superheroapi.com/api/{TOKEN}/search/{hero}"
        response = requests.get(url)
        hero_int[hero] = (int(response.json()['results'][0]['powerstats']['intelligence']))
    return hero_int


def smartest_hero(hero_int):
    v = list(hero_int.values())
    k = list(hero_int.keys())
    best_hero = k[v.index(max(v))]
    print(f'Самый умный супергерой: {best_hero}')
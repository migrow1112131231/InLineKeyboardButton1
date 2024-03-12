from handbook import handbook
from keyboards import buttons_for_game
import random
import requests

def random_box():
    # название button_1, button_2
    box = random.choice(list(buttons_for_game))
    return buttons_for_game[box].callback_data

def send_cat():
    cat: requests.Response = requests.get('https://api.thecatapi.com/v1/images/search')
    return cat.json()[0]['url']
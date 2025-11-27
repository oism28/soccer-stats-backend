
import os
from dotenv import load_dotenv
import requests

load_dotenv()


BASE_URL = os.getenv('BASE_URL')

def get_competiciones():
    print(BASE_URL)
    response = requests.get(f"{BASE_URL}/competitions", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return response.json()


def get_competiciones_by_id(competition_id):
    response = requests.get(f"{BASE_URL}/competitions/{competition_id}", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return response.json()


def get_tabla_competicion(competition_id):
    response = requests.get(f"{BASE_URL}/competitions/{competition_id}/standings", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return response.json()

def get_partidos(competition_id):
    response = requests.get(f"{BASE_URL}/competitions/{competition_id}/matches", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return response.json()


def get_competiciones_equipos(competition_id):
    response = requests.get(f"{BASE_URL}/competitions/{competition_id}/teams", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return response.json()


def get_goleadores(competition_id):
    response = requests.get(f"{BASE_URL}/competitions/{competition_id}/scorers", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return response.json()
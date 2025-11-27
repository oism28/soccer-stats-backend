

import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def obtener_persona(jugador_id):
    respuesta = requests.get(f"{BASE_URL}/persons/{jugador_id}", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return respuesta.json()


def obtener_partidos_persona(jugador_id):
    respuesta = requests.get(f"{BASE_URL}/persons/{jugador_id}/matches", headers={
        "X-Auth-Token": os.getenv("API_KEY")
    })
    return respuesta.json()
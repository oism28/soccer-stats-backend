import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

def obtener_equipo(equipo_id):
	respuesta = requests.get(f"{BASE_URL}/teams/{equipo_id}", headers={
		"X-Auth-Token": os.getenv("API_KEY")
	})
	return respuesta.json()

def listar_equipos():
	equipos = []
	offset = 0
	limite = 100
	while True:
		parametros = {"limit": limite, "offset": offset}
		respuesta = requests.get(f"{BASE_URL}/teams", headers={
			"X-Auth-Token": os.getenv("API_KEY")
		}, params=parametros)
		datos = respuesta.json()
		if "teams" in datos:
			equipos.extend(datos["teams"])
			if len(datos["teams"]) < limite:
				break
			offset += limite
		else:
			break
	return {"equipos": equipos}

def obtener_partidos_equipo(equipo_id):
	respuesta = requests.get(f"{BASE_URL}/teams/{equipo_id}/matches", headers={
		"X-Auth-Token": os.getenv("API_KEY")
	})
	return respuesta.json()



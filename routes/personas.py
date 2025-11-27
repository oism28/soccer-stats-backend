from flask import Blueprint
from api.personas import obtener_persona, obtener_partidos_persona
from utils.jwt_required import jwt_required

personas_bp = Blueprint('personas', __name__)

@personas_bp.route('/personas/<int:jugador_id>')
@jwt_required
def persona(jugador_id, usuario_id=None):
	return obtener_persona(jugador_id)

@personas_bp.route('/personas/<int:jugador_id>/partidos')
@jwt_required
def persona_partidos(jugador_id, usuario_id=None):
	return obtener_partidos_persona(jugador_id)

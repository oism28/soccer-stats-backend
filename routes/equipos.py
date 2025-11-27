from flask import Blueprint
from api.equipos import obtener_equipo, listar_equipos, obtener_partidos_equipo
from utils.jwt_required import jwt_required

equipos_bp = Blueprint('equipos', __name__)

@equipos_bp.route('/equipos')
@jwt_required
def equipos(usuario_id=None):
	return listar_equipos()

@equipos_bp.route('/equipos/<int:equipo_id>')
@jwt_required
def equipo(equipo_id, usuario_id=None):
	return obtener_equipo(equipo_id)

@equipos_bp.route('/equipos/<int:equipo_id>/partidos')
@jwt_required
def equipo_partidos(equipo_id, usuario_id=None):
	return obtener_partidos_equipo(equipo_id)

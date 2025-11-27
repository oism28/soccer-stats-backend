    

from flask import Blueprint
from api.competiciones import get_competiciones, get_competiciones_by_id, get_competiciones_equipos, get_tabla_competicion, get_partidos, get_goleadores
from utils.jwt_required import jwt_required

competiciones_bp = Blueprint('competiciones', __name__)

@competiciones_bp.route('/competiciones')
@jwt_required
def competiciones(usuario_id=None):
    return get_competiciones()

@competiciones_bp.route('/competiciones/<int:competition_id>')
@jwt_required
def competicion(competition_id, usuario_id=None):
    print("competition_id:", competition_id)
    return get_competiciones_by_id(competition_id)

@competiciones_bp.route('/competiciones/<int:competition_id>/posiciones')
@jwt_required
def competicion_posiciones(competition_id, usuario_id=None):
    print("competition_id:", competition_id)
    return get_tabla_competicion(competition_id)


@competiciones_bp.route('/competiciones/<int:competition_id>/partidos')
@jwt_required
def competicion_partidos(competition_id, usuario_id=None):
    print("competition_id:", competition_id)
    return get_partidos(competition_id)




@competiciones_bp.route('/competiciones/<int:competition_id>/teams')
@jwt_required
def competicion_teams(competition_id, usuario_id=None):
    print("competition_id:", competition_id)
    return get_competiciones_equipos(competition_id)


@competiciones_bp.route('/competiciones/<int:competition_id>/goleadores')
@jwt_required
def competicion_goleadores(competition_id, usuario_id=None):
    print("competition_id:", competition_id)
    return get_goleadores(competition_id)


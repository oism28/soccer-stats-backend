from flask import Blueprint, request, jsonify
from utils.jwt_required import jwt_required
from sqlalchemy.orm import sessionmaker
from db import connect_db
from models.jugadores_favoritos import JugadorFavorito, Base

favoritos_personas_bp = Blueprint('favoritos_personas', __name__)
engine = connect_db()
Session = sessionmaker(bind=engine)

@favoritos_personas_bp.route('/favoritos-personas', methods=['POST'])
@jwt_required
def crear_favorito_persona(usuario_id):
    data = request.get_json()
    jugador_id = data.get('jugador_id')
    if not jugador_id:
        return jsonify({'error': 'jugador_id requerido'}), 400
    session = Session()
    existe = session.query(JugadorFavorito).filter_by(jugador_id=jugador_id, usuario_id=usuario_id).first()
    if existe:
        return jsonify({'error': 'Ya es favorito'}), 400
    favorito = JugadorFavorito(jugador_id=jugador_id, usuario_id=usuario_id)
    session.add(favorito)
    session.commit()
    return jsonify({'jugador_id': jugador_id}), 201

@favoritos_personas_bp.route('/favoritos-personas', methods=['GET'])
@jwt_required
def listar_favoritos_personas(usuario_id):
    session = Session()
    favoritos = session.query(JugadorFavorito).filter_by(usuario_id=usuario_id).all()
    ids = [f.jugador_id for f in favoritos]
    return jsonify({'favoritos': ids})

@favoritos_personas_bp.route('/favoritos-personas/<int:jugador_id>', methods=['DELETE'])
@jwt_required
def eliminar_favorito_persona(jugador_id, usuario_id):
    session = Session()
    favorito = session.query(JugadorFavorito).filter_by(jugador_id=jugador_id, usuario_id=usuario_id).first()
    if not favorito:
        return jsonify({'error': 'No existe favorito'}), 404
    session.delete(favorito)
    session.commit()
    return jsonify({'message': 'Favorito persona eliminado', 'jugador_id': jugador_id})

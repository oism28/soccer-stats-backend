from flask import Blueprint, request, jsonify
from utils.jwt_required import jwt_required
from sqlalchemy.orm import sessionmaker
from db import connect_db
from models.equipos_favoritos import EquipoFavorito, Base


equipos_favoritos_bp = Blueprint('equipos_favoritos', __name__)
engine = connect_db()
Session = sessionmaker(bind=engine)


@equipos_favoritos_bp.route('/equipos-favoritos', methods=['POST'])
@jwt_required
def crear_equipo_favorito(usuario_id):
    data = request.get_json()
    equipo_id = data.get('equipo_id')
    if not equipo_id:
        return jsonify({'error': 'equipo_id requerido'}), 400
    session = Session()
    existe = session.query(EquipoFavorito).filter_by(equipo_id=equipo_id, usuario_id=usuario_id).first()
    if existe:
        return jsonify({'error': 'Ya es favorito'}), 400
    favorito = EquipoFavorito(equipo_id=equipo_id, usuario_id=usuario_id)
    session.add(favorito)
    session.commit()
    return jsonify({'equipo_id': equipo_id}), 201


@equipos_favoritos_bp.route('/equipos-favoritos', methods=['GET'])
@jwt_required
def listar_equipos_favoritos(usuario_id):
    session = Session()
    favoritos = session.query(EquipoFavorito).filter_by(usuario_id=usuario_id).all()
    ids = [f.equipo_id for f in favoritos]
    return jsonify({'favoritos': ids})


@equipos_favoritos_bp.route('/equipos-favoritos/<int:equipo_id>', methods=['DELETE'])
@jwt_required
def eliminar_equipo_favorito(equipo_id, usuario_id):
    session = Session()
    favorito = session.query(EquipoFavorito).filter_by(equipo_id=equipo_id, usuario_id=usuario_id).first()
    if not favorito:
        return jsonify({'error': 'No existe favorito'}), 404
    session.delete(favorito)
    session.commit()
    return jsonify({'message': 'Equipo favorito eliminado', 'equipo_id': equipo_id})


from flask import Blueprint, request, jsonify
from utils.jwt_required import jwt_required
from sqlalchemy.orm import sessionmaker
from db import connect_db
from models.competiciones_favoritas import CompeticionFavorita, Base


competiciones_favoritas_bp = Blueprint('competiciones_favoritas', __name__)
engine = connect_db()
Session = sessionmaker(bind=engine)



@competiciones_favoritas_bp.route('/competiciones-favoritas', methods=['POST'])
@jwt_required
def crear_competicion_favorita(usuario_id):
	data = request.get_json()
	competition_id = data.get('competicion_id')
	if not competition_id:
		return jsonify({'error': 'competicion_id requerido'}), 400
	session = Session()
	existe = session.query(CompeticionFavorita).filter_by(competicion_id=competition_id, usuario_id=usuario_id).first()
	if existe:
		return jsonify({'error': 'Ya es favorita'}), 400
	favorito = CompeticionFavorita(competicion_id=competition_id, usuario_id=usuario_id)
	session.add(favorito)
	session.commit()
	return jsonify({ 'competicion_id': competition_id}), 201


@competiciones_favoritas_bp.route('/competiciones-favoritas', methods=['GET'])
@jwt_required
def listar_competiciones_favoritas(usuario_id):
	session = Session()
	favoritos = session.query(CompeticionFavorita).filter_by(usuario_id=usuario_id).all()
	ids = [f.competicion_id for f in favoritos]
	return jsonify({'favoritas': ids})


@competiciones_favoritas_bp.route('/competiciones-favoritas/<int:competition_id>', methods=['DELETE'])
@jwt_required
def eliminar_competicion_favorita(competition_id, usuario_id):
	session = Session()
	favorito = session.query(CompeticionFavorita).filter_by(competicion_id=competition_id, usuario_id=usuario_id).first()
	if not favorito:
		return jsonify({'error': 'No existe favorita'}), 404
	session.delete(favorito)
	session.commit()
	return jsonify({'message': 'Competición favorita eliminada', 'competicion_id': competition_id})

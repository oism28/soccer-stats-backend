from flask import Blueprint, request, jsonify, make_response
from utils.jwt_required import jwt_required
import jwt
import datetime
import os
from sqlalchemy.orm import sessionmaker
from db import connect_db
from models.usuario import Usuario, Base
from werkzeug.security import generate_password_hash, check_password_hash

usuarios_bp = Blueprint('usuarios', __name__)


engine = connect_db()
Session = sessionmaker(bind=engine)
SECRET_KEY = os.getenv('JWT_SECRET', 'supersecretkey')

@usuarios_bp.route('/usuarios/registrar', methods=['POST'])
def registro():
    data = request.get_json()
    nombre = data.get('nombre')
    correo = data.get('correo')
    contrasena = data.get('contrasena')
    session = Session()
    if session.query(Usuario).filter_by(correo=correo).first():
        return jsonify({'error': 'El correo ya está registrado'}), 400
    contrasena_hash = generate_password_hash(contrasena)
    usuario = Usuario(nombre=nombre, correo=correo, contrasena=contrasena_hash)
    session.add(usuario)
    session.commit()

    token = jwt.encode({
        'id': usuario.id,
        'exp': (datetime.datetime.utcnow() + datetime.timedelta(hours=2)).timestamp()
    }, SECRET_KEY, algorithm='HS256')
    if isinstance(token, bytes):
        token = token.decode('utf-8')
    resp = make_response({
        'id': usuario.id,
        'nombre': usuario.nombre,
        'correo': usuario.correo,
        'token': token
    })
    resp.set_cookie('soccer-stats-token', token, httponly=True)
    return resp, 201

@usuarios_bp.route('/usuarios/login', methods=['POST'])
def login():
    data = request.get_json()
    correo = data.get('correo')
    contrasena = data.get('contrasena')
    session = Session()
    usuario = session.query(Usuario).filter_by(correo=correo).first()
    if usuario and check_password_hash(usuario.contrasena, contrasena):
        token = jwt.encode({
            'id': usuario.id,
            'exp': (datetime.datetime.utcnow() + datetime.timedelta(hours=2)).timestamp()
        }, SECRET_KEY, algorithm='HS256')
        if isinstance(token, bytes):
            token = token.decode('utf-8')
        resp = make_response({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'correo': usuario.correo,
            'token': token
        })
        resp.set_cookie('soccer-stats-token', token, httponly=True)
        return resp, 200
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401



@usuarios_bp.route('/usuarios', methods=['GET'])
@jwt_required
def get_data(usuario_id):
    session = Session()
    usuario = session.query(Usuario).get(usuario_id)
    if usuario:
        return jsonify({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'correo': usuario.correo
        }), 200
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404



@usuarios_bp.route('/usuarios/logout', methods=['POST'])
def logout():
    resp = make_response({'message': 'Logout exitoso'})
    resp.set_cookie('soccer-stats-token', '', expires=0, httponly=True)
    return resp, 200

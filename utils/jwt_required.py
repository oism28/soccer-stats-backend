import jwt
import os
import datetime
from flask import request, jsonify
from functools import wraps

SECRET_KEY = os.getenv('JWT_SECRET', 'supersecretkey')

# Decorador para proteger rutas usando JWT en cookie
def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('soccer-stats-token')
        if not token:
            return jsonify({'error': 'Token no encontrado'}), 401
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            exp = payload.get('exp')
            if exp and datetime.datetime.utcnow().timestamp() > exp:
                return jsonify({'error': 'Token expirado'}), 401
            usuario_id = payload['id']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido'}), 401
        return f(usuario_id=usuario_id, *args, **kwargs)
    return decorated_function

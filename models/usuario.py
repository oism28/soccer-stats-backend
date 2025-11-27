from sqlalchemy import Column, Integer, String
from models.base import Base

class Usuario(Base):
	__tablename__ = 'usuarios'

	id = Column(Integer, primary_key=True, autoincrement=True)
	nombre = Column(String(100), nullable=False)
	correo = Column(String(120), unique=True, nullable=False)
	contrasena = Column(String(512), nullable=False)

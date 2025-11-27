from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from models.base import Base

class EquipoFavorito(Base):
    __tablename__ = 'equipos_favoritos'
    __table_args__ = (
        UniqueConstraint('equipo_id', 'usuario_id', name='uq_equipo_usuario'),
    )

    equipo_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)

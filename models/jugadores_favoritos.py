from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from models.base import Base

class JugadorFavorito(Base):
    __tablename__ = 'jugadores_favoritos'
    __table_args__ = (
        UniqueConstraint('jugador_id', 'usuario_id', name='uq_jugador_usuario'),
    )

    jugador_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)

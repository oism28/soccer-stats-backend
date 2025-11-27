from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from models.base import Base

class CompeticionFavorita(Base):
    __tablename__ = 'competiciones_favoritas'
    __table_args__ = (
        UniqueConstraint('competicion_id', 'usuario_id', name='uq_competicion_usuario'),
    )

    competicion_id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), primary_key=True)

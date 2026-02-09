'''tabelas Cliente, Servico e Agendamento'''

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func
from app.database.database import Base
import enum

class UserType(str, enum.Enum):
    CLIENTE = "cliente"
    BARBEIRO = "barbeiro"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    telefone = Column(String(20), nullable=False)
    senha_hash = Column(String(255), nullable=False)
    tipo = Column(Enum(UserType), default=UserType.CLIENTE, nullable=False)
    ativo = Column(Boolean, default=True)
    foto_perfil = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

print("Testando o models")
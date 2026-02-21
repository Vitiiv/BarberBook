'''tabelas Cliente, Servico e Agendamento'''

from sqlalchemy.sql import func
from app.database.database import Base
import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, ForeignKey, Text, Time, JSON, Float

class UserType(str, enum.Enum):
    CLIENTE = "cliente"
    BARBEIRO = "barbeiro"
    ADMIN = "admin"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=False, nullable=False)
    phone = Column(String(20), nullable=False)
    password_hash = Column(String(255), nullable=False)
    user_type = Column(Enum(UserType), default=UserType.CLIENTE, nullable=False)
    active = Column(Boolean, default=True)
    profile_picture = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
class Barbers(Base):
    __tablename__ = "barbers"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)


'''criar a conexao com o SQLite e a sessao do banco.'''

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus


original_password = 'postgres'
encrypted_password = quote_plus(original_password)

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{encrypted_password}@localhost:5432/barberbook"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False )

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    Base.metadata.create_all(bind=engine)
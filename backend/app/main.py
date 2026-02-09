'rodar programa = uvicorn main:app --reload'

from fastapi  import FastAPI
from app.database.database import engine, Base, create_tables
from app.models import models

app = FastAPI()

create_tables()

@app.get('/')
def home():
    return {"Backend funcionando"}
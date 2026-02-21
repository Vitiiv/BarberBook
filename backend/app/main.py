'rodar programa = uvicorn app.main:app --reload'

from fastapi  import FastAPI
from app.database.database import engine, Base, create_tables
from app.models import models
from app.auth import router as auth_router

app = FastAPI()

create_tables()

app.include_router(auth_router)

@app.get('/')
def home():
    return {"Backend funcionando"}

@app.get('/health-check')
def health_check():

    print('============== ROTA ACESSADA - OK ===================')
    
    return {"status": "ROTA ACESSADA - OK"}

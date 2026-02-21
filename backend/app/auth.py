from fastapi import APIRouter
from app.schemas import UserSignUp
import bcrypt
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database.database import get_db
from app.models.models import User

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/sign-up")
def user_register(data: UserSignUp, db: Session = Depends(get_db)):
    
    pwd_byt = data.password.encode('utf-8')
    salt = bcrypt.gensalt() # O salt é um dado aleatório que torna o hash único
    pwd_hash = bcrypt.hashpw(pwd_byt, salt).decode('utf-8')

    new_user = User(
        name = data.name,
        email = data.email,
        phone = data.phone,
        password_hash = pwd_hash
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "mensagem": "JSON recebido com sucesso",
    }
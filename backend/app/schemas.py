from pydantic import BaseModel

class UserSignUp(BaseModel):
    name: str
    email: str
    phone: str
    password: str
    userType: str
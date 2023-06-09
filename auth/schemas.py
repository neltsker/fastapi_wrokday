from pydantic import EmailStr, BaseModel, UUID4
from typing import Optional


class UserResponceSchema(BaseModel):
    usernam:str
    email: str#Optional[str] = ormar.String(max_length=100)
    full_name: str#Optional[str] = ormar.String(max_length=100)
    disabled: bool#Optional[bool] = ormar.Boolean()
    #latitude: float
    #longitude: float
    
class UserRegistrationSchema(BaseModel):
    username:str
    email: str#Optional[str] = ormar.String(max_length=100)
    full_name: str#Optional[str] = ormar.String(max_length=100)
    password: str
    password2: str
    
    #disabled: bool#Optional[bool] = ormar.Boolean()
    #latitude: float
    #longitude: float
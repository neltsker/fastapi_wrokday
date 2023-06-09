from fastapi import APIRouter, Response, status
from starlette.requests import Request
#from starlette.templating import Jinja2Templates
#from .validators import UserValidator
from pydantic import BaseModel
import ormar
from db import metadata, database
from typing import List, Optional




fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


class Token(ormar.Model):
    class Meta:
        tablename = 'tokens'
        metadata = metadata
        database = database
    id: Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    access_token: str = ormar.String(max_length=10000)
    token_type: str = ormar.String(max_length=100)


class TokenData(ormar.Model):
    class Meta:
        tablename = 'tokensdata'
        metadata = metadata
        database = database
    id: Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    username: Optional[str] = ormar.String(max_length=1000)


class User(ormar.Model):
    class Meta:
        tablename = 'users'
        metadata = metadata
        database = database
    id: Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    username: str = ormar.String(max_length=100)
    email: Optional[str] = ormar.String(max_length=100)
    full_name: Optional[str] = ormar.String(max_length=100)
    disabled: Optional[bool] = ormar.Boolean()
    hashed_password: str= ormar.String(max_length=10000)


#class UserInDB(User, ormar.Model):


"""
class User(ormar.Model):
    class Meta:
        tablename = 'users'
        metadata = metadata
        database = database
        
    id : Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    firstName: str = ormar.String(max_length=100)
"""
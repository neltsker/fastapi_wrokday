from fastapi import APIRouter, Response, status
from starlette.requests import Request
from pydantic import BaseModel
import ormar
from db import metadata, database
from typing import List, Optional
from auth.models import User
from datetime import datetime, timedelta




class Organization(ormar.Model):
    class Meta:
        tablename = 'organizations'
        metadata = metadata
        database = database
    id: Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    name: str = ormar.String(max_length=100)
    description: str = ormar.String(max_length=1000)
    creator: User = ormar.ForeignKey(User)


class Department(ormar.Model):
    class Meta:
        tablename = 'department'
        metadata = metadata
        database = database
    id: Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    name: str = ormar.String(max_length=100)
    admin: List[User] = ormar.ForeignKey(User, related_name='admin')
    organization: Organization = ormar.ForeignKey(Organization)
    workers: Optional[List[User]] =ormar.ForeignKey(User, related_name='worker')



class Task(ormar.Model):
    class Meta:
        tablename = 'tasks'
        metadata = metadata
        database = database
    id: Optional[int] = ormar.Integer(primary_key=True, autoincrement=True)
    name: str = ormar.String(max_length=100)
    description: Optional[str] = ormar.String(max_length=100)
    startDate: datetime = ormar.DateTime(default=datetime.now())
    endDate: Optional[datetime] = ormar.DateTime(nullable=True)
    creator: User = ormar.ForeignKey(User, related_name="creator")
    worker: User = ormar.ForeignKey(User)
    dep: Department = ormar.ForeignKey(Department)
    #state:
    
    #full_name: Optional[str] = ormar.String(max_length=100)
    #disabled: Optional[bool] = ormar.Boolean()
    #hashed_password: str= ormar.String(max_length=10000)


"""
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
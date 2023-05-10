from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi import APIRouter, Response, status
from .models import  *
from .schemas import *
from db import database, metadata, engine


task_router = APIRouter(prefix="/task",
                        tags=["task"])


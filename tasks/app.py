from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from fastapi import APIRouter, Response, status
from .models import  *
from .schemas import *
from db import database, metadata, engine
from auth.app import get_current_active_user


task_router = APIRouter(prefix="/task",
                        tags=["task"])


@task_router.get("/")
async def hi():
    return "hi"


@task_router.get("/organizations")
async def organizations(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

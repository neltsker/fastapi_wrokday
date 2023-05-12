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


@task_router.get("/org/list")
async def organizations(current_user: Annotated[User, Depends(get_current_active_user)]):
    organs = await Organization.objects.all()
    return {"organs": organs}
    return current_user

@task_router.get("/dep/list")
async def organizations(current_user: Annotated[User, Depends(get_current_active_user)], id:int):
    organs = await Organization.objects.filter(organization.id ==id).all()
    return {"organs": organs}

@task_router.post("/org")#, response_model=UserResponceSchema)
async def OrganizationRegistration(current_user: Annotated[User, Depends(get_current_active_user)], org: OrgRegistrationSchema):
    #form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    #user = await authenticate_user(form_data.username, form_data.password)
    #print(user)
    #userDB = await User.objects.get_or_none(username=user.username)
    organDB= await Organization.objects.get_or_none(name=org.name)
    if not organDB:
        organ=Organization(
            name=org.name,
            description=org.description,
            creator=current_user.id
            )
        await organ.save()
        return organ
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Organization already exist",
            #headers={"WWW-Authenticate": "Bearer"},
        )
    return "i don't know"
    """"
    if not userDB:
        hashPassword = get_password_hash(user.password)
        userSave=User( 
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashPassword,
        disabled=False)

        await userSave.save()
        await authenticate_user(userSave.username, user.password)
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exist",
            #headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    """
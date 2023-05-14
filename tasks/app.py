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
    organs = await Department.objects.filter(organization__id=id).all()
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

@task_router.post("/dep")#, response_model=UserResponceSchema)
async def DepartmentRegistration(current_user: Annotated[User, Depends(get_current_active_user)], dep: DepRegistrationSchema):
    #form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    #user = await authenticate_user(form_data.username, form_data.password)
    #print(user)
    #userDB = await User.objects.get_or_none(username=user.username)
    depDB= await Department.objects.filter(organization__id=dep.organization).get_or_none(name=dep.name)
    if not depDB:
        depar=Department(
            name=dep.name,
            organization = dep.organization,
            admin=dep.admin
            )
        await depar.save()
        return depar
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Department already exist",
            #headers={"WWW-Authenticate": "Bearer"},
        )
    return "i don't know"

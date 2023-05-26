from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from db import database, metadata, engine


from auth.app import user_router, oauth2_scheme
from tasks.app import task_router

"""
FastApiWorkDay Server app.
Fastapi wsgi app
Created by:
Kurbanov Roman PE-01b
Ivanov Oleg PE-01b
Evdokimov Sergey PE-01b

"""


app = FastAPI()


metadata.create_all(engine)
app.state.database = database
#metadata.create_all(database)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()

    


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


"""
metadata.create_all(engine)
app.state.database = database
#metadata.create_all(database)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
"""

app.include_router(user_router)
app.include_router(task_router)



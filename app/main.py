import datetime, uuid
from .pg_db import database, users, engine
from fastapi import FastAPI
from typing import List
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from typing import Optional
from fastapi.responses import ORJSONResponse
from fastapi import status, HTTPException



class UserList(BaseModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    username  : str
  
class UserEntry(BaseModel):
    username  : str = Field(..., example="potinejj")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI(
    docs_url="/api/v2/docs",
    redoc_url="/api/v2/redocs",
    title="Core API",
    description="New Framework of Python",
    version="2.0",
    openapi_url="/api/v2/openapi.json",
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/users", response_model=List[UserList], tags=["Users"])
async def find_all_users():
    query = users.select()
    return await database.fetch_all(query)

@app.post("/users", tags=["Users"])
async def register_user(user: UserEntry):
    gDate = str(datetime.datetime.now())

    query2 = users.select().where(users.c.username == user.username)
    existing = await database.execute(query2)
    print(existing)

    if str(existing).isnumeric():
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f'User already existed',
        )  
    else:
        query = users.insert().values(
            username   = user.username
        )        
        id = await database.execute(query)
        return {
            "id": id,
            **user.dict(),
            "create_at":gDate
        }              

@app.get("/users/{user_name}", response_model=UserList, tags=["Users"])
async def find_user_by_id(user_name: str):
    query = users.select().where(users.c.username == user_name)
    return await database.fetch_one(query)

@app.delete("/users/{user_name}", tags=["Users"])
async def delete_user(user_name: str):
    query = users.delete().where(users.c.username == user_name)
    await database.execute(query)

    return {
        "status" : True,
        "message": "This user has been deleted successfully." 
    }
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.user import UserSchema
from models.user import User as UserModel
from config.database import engine
from sqlmodel import Session
from typing import List
from services.user import UserService

router = APIRouter(
    prefix="/api/users",
    tags=["users"]
)

# endpoint get all users
@router.get("/")
async def get_users() -> List[UserSchema]:
    db = Session(engine)
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# endpoint get an user
@router.get("/{id}", tags=["users"], response_model=UserSchema)
def get_user(id: int = Path(ge=1)) -> UserSchema:
    db = Session(engine)
    result = UserService(db).get_user(id)
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

# endpoint create user
@router.post("/", tags=["users"], response_model=dict, status_code=201)
async def create_users(user: UserSchema) -> dict:
    # crear una sesion para conectarme a la base de datos
    db = Session(engine)
    UserService(db).create_user(user)
    #users.append(jsonable_encoder(user))
    return JSONResponse(status_code=201, content={"message": "Se ha registro el usuario"})

# update a user
@router.put("/{id}", tags=["users"], response_model=dict, status_code=200)
def update_user(id: int, user: UserSchema) -> dict:
    db = Session(engine)
    result = UserService(db).update_user(id, user)
    return JSONResponse(status_code=200, content=result)

# delete user
@router.delete("/{id}", tags=["users"], response_model=dict, status_code=200)
def delete_user(id: int) -> dict:
    db = Session(engine)
    result = UserService(db).delete_user(id)
    return JSONResponse(status_code=200, content=result)


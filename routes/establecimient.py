from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.establecimient import Establecimient as EstablecimientModel
from schemas.establecimient import EstablecimientSchema
from config.database import engine
from sqlmodel import Session
from typing import List
from middlewares.auth_handler import JWTBearer

router = APIRouter(
    prefix="/api/establecimients",
    tags=["establecimients"]
)

# get establecimients
@router.get("/", response_model=list[EstablecimientSchema])
def get_establecimients() -> List[EstablecimientSchema]:
    db = Session(engine)
    result = db.query(EstablecimientModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# get an establecimient 
@router.get("/{id}", response_model=EstablecimientSchema)
def get_establecimient(id: int = Path(ge=1))-> EstablecimientSchema:
    db = Session(engine)
    result = db.query(EstablecimientModel).filter(EstablecimientModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "establecimient not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# create establecimients, proteccion inicial de esta ruta
@router.post("/", tags=["establecimients"], response_model=dict, status_code=201, dependencies=[Depends(JWTBearer())])
def create_establecimients(establecimient: EstablecimientSchema):
    # crear una sesion para conectarme a la base de datos
    db = Session(engine)
    new_establecimient = EstablecimientModel(**establecimient.dict())
    db.add(new_establecimient)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registro el establecimiento"})

@router.put("/{id}", tags=["establecimients"], response_model=dict, status_code=200)
def update_establecimient(id: int, establecimient: EstablecimientSchema) -> dict:
    db = Session(engine)
    result = db.query(EstablecimientModel).filter(EstablecimientModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "establecimient not found"})
    result.first_name = establecimient.name
    result.last_name = establecimient.ciudad
    result.dni = establecimient.briefcase_id
    result.email = establecimient.state
    # seve data
    db.commit()
    return JSONResponse(status_code=200, content={"message": "establecimient update with success"})

@router.delete("/{id}", tags=["establecimients"], response_model=dict, status_code=200)
def delete_establecimient(id: int) -> dict:
    db = Session(engine)
    result = db.query(EstablecimientModel).filter(EstablecimientModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "establecimient not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "establecimient delete with success"})
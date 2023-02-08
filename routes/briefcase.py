from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.briefcase import Briefcase as BriefcaseModel
from models.product import Product as ProductModel
from schemas.briefcase import BriefcaseSchema
from config.database import engine
from sqlmodel import Session
from typing import List

router = APIRouter(
    prefix="/api/briefcases",
    tags=["briefcases"]
)

@router.get("/", response_model=list[BriefcaseSchema])
def get_briefcase() -> List[BriefcaseSchema]:
    db = Session(engine)
    result = db.query(BriefcaseModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# endpoint get a briefcase (portafolio de productos)
@router.get("/{id}", tags=["briefcases"], response_model=BriefcaseSchema)
def get_briefcase(id: int = Path(ge=1)) -> BriefcaseSchema:
    db = Session(engine)
    result = db.query(BriefcaseModel).filter(BriefcaseModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "Briefcase not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

# endpoint create a briefcase (portafolio de productos)
@router.post("/", tags=["briefcases"], response_model=dict, status_code=201)
async def create_products(briefcase: BriefcaseSchema) -> dict:
    # crear una sesion para conectarme a la base de datos
    db = Session(engine)
    new_briefcase = BriefcaseModel(**briefcase.dict())
    db.add(new_briefcase)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "briefcase register with success"})

# update a briefcase (portafolio de productos)
@router.put("/{id}", tags=["briefcases"], response_model=dict, status_code=200)
def update_movie(id: int, briefcase: BriefcaseSchema) -> dict:
    db = Session(engine)
    result = db.query(BriefcaseModel).filter(BriefcaseModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "briefcase not found"})
    result.name = briefcase.name
    result.state = briefcase.state
    # seve data
    db.commit()
    return JSONResponse(status_code=200, content={"message": "briefcase update with success"})

# delete briefcase (portafolio de productos)
@router.delete("/{id}", tags=["briefcases"], response_model=dict, status_code=200)
def delete_briefcase(id: int) -> dict:
    db = Session(engine)
    result = db.query(BriefcaseModel).filter(BriefcaseModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"message": "briefcase not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "product delete with success"})

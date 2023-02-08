from fastapi import APIRouter, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models.product import Product as ProductModel
from schemas.product import ProductSchema
from config.database import engine
from sqlmodel import Session
from typing import List
from services.product import ProductService
# from middlewares.auth_handler import JWTBearer

router = APIRouter(
    prefix="/api/products",
    tags=["products"]
)

@router.get("/", response_model=list[ProductSchema])
def get_products() -> List[ProductSchema]:
    db = Session(engine)
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# endpoint get a product
@router.get("/{id}", tags=["products"], response_model=ProductSchema)
def get_product(id: int = Path(ge=1)) -> ProductSchema:
    db = Session(engine)
    return ProductService(db).get_product(id)
    return JSONResponse(status_code=200,content=jsonable_encoder(result))

# endpoint create a product
@router.post("/", tags=["products"], response_model=dict, status_code=201)
async def create_products(product: ProductSchema) -> dict:
    # crear una sesion para conectarme a la base de datos
    db = Session(engine)
    ProductService(db).create_product(product)
    return JSONResponse(status_code=201, content={"message": "product register with success"})

# update a product
@router.put("/{id}", tags=["products"], response_model=dict, status_code=200)
def update_product(id: int, product: ProductSchema) -> dict:
    db = Session(engine)
    result = ProductService(db).update_product(id, product)
    return JSONResponse(status_code=200, content=result)

# delete product
@router.delete("/{id}", tags=["products"], response_model=dict, status_code=200)
def delete_product(id: int) -> dict:
    db = Session(engine)
    result = ProductService(db).delete_product(id)
    return JSONResponse(status_code=200, content=result)

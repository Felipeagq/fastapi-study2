from fastapi import FastAPI 
from fastapi.responses import JSONResponse
import uvicorn
from routes import user, product, briefcase, establecimient
from config.database import engine
from sqlmodel import SQLModel, Session
from middlewares.error_handler import ErrorHandler
from schemas.user import UserSchema
from jwt_manager import create_token, validate_token
from models.user import User as UserModel

app = FastAPI(title="Api POS", version="0.0.1")

app.add_middleware(ErrorHandler)

SQLModel.metadata.create_all(engine)

# register of routes
app.include_router(user.router)
app.include_router(product.router)
app.include_router(briefcase.router)
app.include_router(establecimient.router)

@app.get("/")
async def root():
    return {"message": "Welcome ApiRest"}

@app.post("/login", tags=["auth"])
def login(user: UserSchema):
    db = Session(engine)
    result = db.query(UserModel).filter(UserModel.id == user.email and UserModel.password == user.password).first()
    if not result:
        return JSONResponse(status_code=403, content={"message": "crendencias invalidos"})
    else:
        #if user.email == result.email and user.password == result.password:
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
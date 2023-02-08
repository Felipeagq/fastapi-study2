from fastapi import Request
from jwt_manager import validate_token
from fastapi.security import HTTPBearer

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        # se obtiene el token
        data = validate_token(auth.credentials)
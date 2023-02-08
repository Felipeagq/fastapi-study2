from jwt import encode, decode
from dotenv import load_dotenv

load_dotenv() # cargandando variables de entorno

def create_token(data: dict):
    token: str = encode(payload=data, key=SECRET_KEY, algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key=SECRET_KEY, algorithms=["HS256"])
    return data
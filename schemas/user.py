from pydantic import BaseModel, Field
from typing import Optional, List

class UserSchema(BaseModel):
    id: Optional[int]
    first_name: str = Field(min_length=5, max_length=150)
    last_name: str = Field(min_length=5, max_length=150)
    dni: int
    email: str = Field(min_length=10, max_length=100)
    password: str = Field(min_length=8, max_length=30)
    state: int

    class Config:
        schema_extra = {
            "example": {
                'first_name': 'Andres',
                'last_name': "Robles",
                'dni': 12554522,
                'email': "micorreo@correo.com",
                'password': 'password123456',
                'state': 1
            }
        }
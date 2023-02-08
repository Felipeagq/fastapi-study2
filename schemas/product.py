from pydantic import BaseModel, Field
from typing import Optional, List

class ProductSchema(BaseModel):
    id: Optional[int]
    name: str = Field(min_length=5, max_length=150)
    image: str = Field(min_length=5)
    tipo: str = Field(default="supermercado")
    state: int

    class Config:
        schema_extra = {
            "example": {
                'name': 'Queso crema',
                'image': 'https://picsum.photos/200/300',
                'tipo': 'supermercado',
                'state': 1
            }
        }
from pydantic import BaseModel, Field
from typing import Optional, List

class EstablecimientSchema(BaseModel):
    establecimient_id: Optional[int]
    name: str = Field(min_length=5, max_length=150)
    briefcase_id: int
    ciudad: str = Field(min_length=5, max_length=50) 
    state: int

    class Config:
        schema_extra = {
            "example": {
                'name': 'supermercado el campeon',
                'briefcase_id': 1,
                'cuidad': 'barranquilla',
                'state': 1
            }
        }
from pydantic import BaseModel, Field
from typing import Optional, List

class BriefcaseSchema(BaseModel):
    id: Optional[int]
    name: str = Field(min_length=5, max_length=150)
    state: int

    class Config:
        schema_extra = {
            "example": {
                'name': 'Portafolio superplus supermercados',
                'state': 1
            }
        }
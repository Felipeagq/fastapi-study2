
from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Briefcase(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    state: int
    #products = relationship("products", secondary='briefcase_product')
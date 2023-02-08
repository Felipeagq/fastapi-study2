from typing import Optional

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    image: str
    tipo: str
    state = int

    # briefcases = relationship("briefcase", secondary='briefcase_product')
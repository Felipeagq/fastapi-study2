from typing import Optional

from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    dni: int
    email: str
    password: str
    state: int
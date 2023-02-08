from typing import Optional

from sqlmodel import Field, SQLModel, create_engine


class Establecimient(SQLModel, table=True):
    establecimient_id: Optional[int] = Field(default=None, primary_key=True)
    briefcase_id: Optional[int] = Field(default=None, foreign_key="briefcase.id")
    name: str
    ciudad: int
    state: int
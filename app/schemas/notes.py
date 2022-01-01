from pydantic import BaseModel

from app.schemas.core import BaseReadSchema


class NoteIn(BaseModel):
    note: str


class NoteOut(BaseReadSchema, NoteIn):
    ...

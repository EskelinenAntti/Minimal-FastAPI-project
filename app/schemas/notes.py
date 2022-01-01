from pydantic import BaseModel

from app.schemas.core import BaseReadSchema


class NoteBase(BaseModel):
    note: str


class NoteOut(BaseReadSchema, NoteBase):
    ...


class NoteIn(NoteBase):
    ...

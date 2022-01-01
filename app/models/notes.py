from sqlalchemy import Column, String
from app.models.core import BaseModel


class Note(BaseModel):
    __tablename__ = "notes"

    note = Column(String)

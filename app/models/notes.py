from sqlalchemy import Column, String, Integer

from app.db import Base


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    note = Column(String)

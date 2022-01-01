from sqlalchemy import Column, String, Integer

from app.db import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

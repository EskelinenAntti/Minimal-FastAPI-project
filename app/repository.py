from typing import Type, Callable

from fastapi import Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db import Base, get_session


class Repository:
    def __init__(self, model: Type[Base], session: Session):
        self.model = model
        self.session = session

    def get(self, skip: int = 0, limit: int = 100):
        return self.session.query(self.model).offset(skip).limit(limit).all()

    def get_by_id(self, id: int):
        return self._get_by_id_or_raise(id)

    def create(self, instance: BaseModel):
        db_instance = self.model(**instance.dict())
        self.session.add(db_instance)
        self.session.commit()
        self.session.refresh(db_instance)
        return db_instance

    def update(self, id: int, instance: BaseModel):
        db_instance = self._get_by_id_or_raise(id)

        for key, value in instance.dict().items():
            setattr(db_instance, key, value)
        self.session.commit()
        self.session.refresh(db_instance)
        return db_instance

    def delete(self, id: int):
        db_instance = self._get_by_id_or_raise(id)
        self.session.delete(db_instance)
        self.session.commit()
        return db_instance

    def _get_by_id_or_raise(self, id: int):
        db_instance = self.session.query(self.model).filter_by(id=id).first()
        if not db_instance:

            # Should not throw HTTP exceptions from repository but let's be lazy.
            raise HTTPException(status_code=404)

        return db_instance

    @staticmethod
    def get_repository(model: Type[Base]) -> Callable[[Session], "Repository"]:
        def _get_repository(session: Session = Depends(get_session)):
            return Repository(model, session)

        return _get_repository

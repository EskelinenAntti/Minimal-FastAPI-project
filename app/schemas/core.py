from pydantic import BaseModel


class BaseReadSchema(BaseModel):
    id: int

    class Config:
        orm_mode = True

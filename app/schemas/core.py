from pydantic import BaseModel
from datetime import datetime


class BaseReadSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

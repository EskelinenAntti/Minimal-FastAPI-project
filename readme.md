# Minimal FastAPI project

This project contains a minimal setup for the following components:

- FastAPI
- SqlAlchemy
- Sqlite

The project is done for learning and research purposes.

## Run the project

Install FastAPI from PIP and run the project with
`uvicorn app.main:app --reload`

#### TODO:

- [ ] Add CRUD layer for DB operations.

## Highlights

### Database configuration

Database related configurations and setup code is encapsulated in `db.py`. The following snippet demonstrates how to
obtain a database session in an API router:

```python
@router.get("/", response_model=list[NoteOut])
async def get_notes(session: Session = Depends(db.get_session)) -> NoteOut:
    return session.query(models.Note).all()
```

The `Depends(db.get_session)` dependency creates the session and closes it automatically on each request.

### Abstract base schema and model with id, created_at and updated_at fields

The project contains an SQLAlchemy base model model with id, created_at and updated_at fields. When a new instance is created or
updated those values are updated automatically in the backend side.

```python
class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
```

Correspondingly, `BaseReadSchema` can be inherited when those values are needed in a Pydantic schema.
```python
class BaseReadSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
```


### Structure

The structure follows roughly this
pattern: https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure
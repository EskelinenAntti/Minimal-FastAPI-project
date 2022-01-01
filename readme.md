# Minimal FastAPI project

This project contains a minimal setup for the following components:

- FastAPI
- SqlAlchemy
- Sqlite

The project is done for learning and research purposes.

## Running:

Install FastAPI from PIP and run the project with
`uvicorn app.main:app --reload`

#### TODO:

- [ ] Add CRUD layer for DB operations.

## Highlights

### Database configuration

Database related configurations and setup code is encapsulated in `db.py`. The following snippet demonstrates how to
obtain a database session in an API router:

```python
@router.get("/", response_model=list[Note])
async def get_notes(session: Session = Depends(db.get_session)):
    return session.query(models.Note).all()
```

The `Depends(db.get_session)` dependency creates the session and closes it automatically on each request.

### Pydantic In and Out schemas

Below we have an example endpoint that allows creating new notes:

```python
@router.post("/", response_model=NoteOut)
async def create_note(payload: NoteIn, session: Session = Depends(db.get_session)) -> NoteOut:
    # store payload in database and return result 
    # code truncated
    return note
```

Notice that the endpoint takes `NoteIn` as request payload and returns `NoteOut`. `NoteIn` contains only the fields that
users can define. `NoteOut` contains in addition the fields whose values are set by the backend, such as `id`.

In this project, the `BaseReadSchema` in `app/schemas/core` can be inherited to define a read only
schema. `BaseReadSchema` defines common read only field values. In addition, it contains the `orm_mode = True`
configuration, which makes it possible to create an instance of the schema from an ORM object.

```python
class BaseReadSchema(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
```

This makes it possible to define the "In" and "Out" schemas with little duplicate code.

```python
class NoteBase(BaseModel):
    note: str


class NoteOut(BaseReadSchema, NoteBase):
    ...


class NoteIn(NoteBase):
    ...
```

Or, if the `in` and the `base` schemas are identical like in the example above, we can go even further and define those
as:

```python
class NoteIn(BaseModel):
    note: str


class NoteOut(BaseReadSchema, NoteIn):
    ...
```

### Structure

The structure follows roughly this
pattern: https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure
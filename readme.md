# Minimal FastAPI project

This project contains a minimal setup for the following components:

- FastAPI
- SqlAlchemy
- Sqlite

The project is done for learning and research purposes.

## Run the project

Install FastAPI from PIP and run the project with
`uvicorn app.main:app --reload`

## Highlights

### Database configuration

Database related configurations and setup code is encapsulated in `db.py`. The following snippet demonstrates how to
obtain a database session:

```python
def _get_repository(session: Session = Depends(get_session)):
    return Repository(model, session)
```

The `Depends(db.get_session)` dependency creates the session and closes it automatically once its no longer needed.

### Generic repository

Similarly, the project contains a generic repository with basic CRUD operations. The repository can be accessed using
FastAPI's dependency injection:

```python
@router.get("/", response_model=list[NoteOut])
async def get_notes(notes: Repository = Depends(Repository.get_repository(Note))):
    return notes.all()
```

### Mypy

Mypy plugin has been configured to work with SQLAlchemy code.

1. Installed stubs with `pip install sqlalchemy[mypy]`
2. Configured mypy plugin to `mypy.ini`
3. Ran mypy with `mypy .`

### Structure

The structure follows roughly this
pattern: https://fastapi.tiangolo.com/tutorial/bigger-applications/#an-example-file-structure
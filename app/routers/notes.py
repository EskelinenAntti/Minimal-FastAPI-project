from fastapi import APIRouter, Depends

from app.models import Note
from app.repository import Repository
from app.schemas.notes import NoteOut, NoteIn

router = APIRouter()


@router.get("/", response_model=list[NoteOut])
async def get_all(
    skip=0, limit=100, notes: Repository = Depends(Repository.get_repository(Note))
):
    return notes.get(skip, limit)


@router.get("/{id}", response_model=NoteOut)
async def get_by_id(id, notes: Repository = Depends(Repository.get_repository(Note))):
    return notes.get_by_id(id)


@router.put("/{id}", response_model=NoteOut)
async def update(
    id, payload: NoteIn, notes: Repository = Depends(Repository.get_repository(Note))
):
    return notes.update(id, payload)


@router.post("/", response_model=NoteOut)
async def post_note(
    payload: NoteIn, notes: Repository = Depends(Repository.get_repository(Note))
) -> NoteOut:
    return notes.create(payload)


@router.delete("/{id}", response_model=NoteOut)
async def delete(id, notes: Repository = Depends(Repository.get_repository(Note))):
    return notes.delete(id)

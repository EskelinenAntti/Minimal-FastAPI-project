from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.notes import NoteOut, NoteIn
from app import db
from app import models

router = APIRouter()


@router.get("/", response_model=list[NoteOut])
async def get_notes(session: Session = Depends(db.get_session)):
    return session.query(models.Note).all()


@router.post("/", response_model=NoteOut)
async def post_note(request_note: NoteIn, session: Session = Depends(db.get_session)) -> NoteOut:
    note = models.Note(**request_note.dict())
    session.add(note)
    session.commit()
    session.refresh(note)
    return note

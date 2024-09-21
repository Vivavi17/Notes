from fastapi import APIRouter, Depends
from typing import Optional, Literal
from src.notes.service import notes_service
from src.users.models import Users
from src.users.jwt_dependencies import get_curr_user
from src.notes.schemas import NewNoteS, NotesS

notes_router = APIRouter(prefix="/notes", tags=["notes"])


@notes_router.get("/")
async def get_notes(limit: Optional[int] = None, offset: Optional[int] = None,
                    order_by: Literal["created_at", "body"] = None,
                    user: Users = Depends(get_curr_user)) -> list[NotesS]:
    return await notes_service.get_notes(user.id, limit, offset, order_by)


@notes_router.post("/")
async def add_note(body: NewNoteS, user: Users = Depends(get_curr_user)) -> NotesS:
    return await notes_service.add_note(user.id, body.body)

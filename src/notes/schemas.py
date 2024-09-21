from datetime import datetime

from pydantic import BaseModel


class NewNoteS(BaseModel):
    body: str


class NotesS(BaseModel):
    body: str
    created_at: datetime

class YaExceptionS(BaseModel):
    code: int
    pos: int
    row: int
    col: int
    len: int
    word: str
    s: list[str]
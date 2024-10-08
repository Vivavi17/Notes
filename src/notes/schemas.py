"""Схемы валидации заметок"""

from datetime import datetime

from pydantic import BaseModel


class NewNoteS(BaseModel):
    """Валидация создания новой заметки"""

    body: str


class NotesS(BaseModel):
    """Валидация на получение заметки"""

    body: str
    created_at: datetime


class YaExceptionS(BaseModel):
    """Модель обработки ошибок текста"""

    code: int
    pos: int
    row: int
    col: int
    len: int
    word: str
    s: list[str]

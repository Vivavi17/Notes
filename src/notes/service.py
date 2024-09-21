from typing import Optional, List

from src.notes.dao import NotesDAO
from src.notes.schemas import NotesS, YaExceptionS
from src.config import settings
import requests
from pydantic import TypeAdapter


def edit_text(text: str, exc: list[YaExceptionS]) -> str:
    j = 0
    words = []
    for i in range(len(exc)):
        words.append(text[j:exc[i].pos])
        words.append(exc[i].s[0])
        j = exc[i].pos + exc[i].len
    words.append(text[j:len(text)])
    return "".join(words)


class NotesService:
    dao = NotesDAO

    async def get_notes(self, author_id: int, limit: Optional[int], offset: Optional[int], order_by: Optional[str]) -> \
            list[NotesS]:
        return await self.dao.find_all(limit, offset, order_by, author_id=author_id)

    async def add_note(self, author_id: int, body: str) -> NotesS:
        response = requests.get(settings.URL_YA_SPELLER_JSON,
                                params={"text": body})
        adapter = TypeAdapter(List[YaExceptionS])
        items = adapter.validate_json(response.content)
        new_body = edit_text(body, items)
        return await self.dao.add(author_id=author_id, body=new_body)


notes_service = NotesService()

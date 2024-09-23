"""Бизнес-логика работы с записями"""
from typing import List, Optional

import requests
from pydantic import TypeAdapter

from src.config import settings
from src.notes.dao import NotesDAO
from src.notes.schemas import NotesS, YaExceptionS

MAX_SIZE_TEXT_REQUEST = 9000


def edit_text(text: str, excs: list[YaExceptionS]) -> str:
    """Изменение текста в зависимости от полученных ошибок"""
    j = 0
    words = []

    for _, exc in enumerate(excs):
        words.append(text[j: exc.pos])
        words.append(exc.s[0])
        j = exc.pos + exc.len
    words.append(text[j : len(text)])
    return "".join(words)


def split_text(text: str) -> list[str]:
    """Делит текст на чанки по пробелам, если пробел не найден добавляет максимальный размер"""
    chunks = []
    if len(text) > MAX_SIZE_TEXT_REQUEST:
        last_pos = curr_pos = 0
        while last_pos != len(text):
            curr_pos += min(MAX_SIZE_TEXT_REQUEST, len(text) - curr_pos)
            while (
                curr_pos != len(text) and curr_pos != last_pos and text[curr_pos] != " "
            ):
                curr_pos -= 1
            if curr_pos != last_pos:
                chunks.append(text[last_pos:curr_pos])
                last_pos = curr_pos
            else:
                chunks.append(text[last_pos:MAX_SIZE_TEXT_REQUEST])
                last_pos += MAX_SIZE_TEXT_REQUEST
                curr_pos = last_pos
        return chunks
    return [text]


class NotesService:
    """Логика работы записок"""
    dao = NotesDAO
    adapter = TypeAdapter(List[YaExceptionS])

    async def get_notes(
        self,
        author_id: int,
        limit: Optional[int],
        offset: Optional[int],
        order_by: Optional[str],
    ) -> list[NotesS]:
        """Получение записок по id пользователя"""
        return await self.dao.find_all(limit, offset, order_by, author_id=author_id)

    async def add_note(self, author_id: int, body: str) -> NotesS:
        """Добавление записки"""
        chunks = split_text(body)
        for i, text in enumerate(chunks):
            try:
                response = requests.get(
                    settings.URL_YA_SPELLER_JSON, params={"text": text}, timeout=10
                )
            except ConnectionError:
                continue
            else:
                if response.status_code == 200:
                    items = self.adapter.validate_json(response.content)
                    chunks[i] = edit_text(text, items)
        new_text = "".join(chunks)
        return await self.dao.add(author_id=author_id, body=new_text)


notes_service = NotesService()

"""Модуль с работой запросов к таблице заметок"""

from src.base.base_dao import BaseDAO
from src.notes.models import Notes


class NotesDAO(BaseDAO):  # pylint: disable=too-few-public-methods
    """Класс с логикой запросов к таблице заметок"""

    model = Notes

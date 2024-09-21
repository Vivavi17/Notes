from src.base.base_dao import BaseDAO
from src.notes.models import Notes


class NotesDAO(BaseDAO):
    model = Notes

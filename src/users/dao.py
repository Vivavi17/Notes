"""Модуль с работой запросов к таблице пользователей"""

from src.base.base_dao import BaseDAO
from src.users.models import Users


class UsersDAO(BaseDAO):  # pylint: disable=too-few-public-methods
    """Класс с логикой запросов к таблице пользователей"""

    model = Users

"""Модуль с кастомными ошибками сервиса"""

from fastapi import HTTPException, status


class NotesExceptions(HTTPException):
    """Базовый класс ошибок"""

    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(NotesExceptions):
    """Ошибка создания пользователя"""

    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class UserDoesntExistsException(NotesExceptions):
    """Ошибка поиска пользователя"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не найден"


class IncorrectLoginOrPasswordException(NotesExceptions):
    """Ошибка поиска пользователя"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный логин или пароль"


class IncorrectTokenFormatException(NotesExceptions):
    """Ошибка токена"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"

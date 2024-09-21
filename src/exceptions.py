from fastapi import HTTPException, status


class NotesExceptions(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(NotesExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class UserDoesntExistsException(NotesExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Пользователь не найден"


class IncorrectLoginOrPasswordException(NotesExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный логин или пароль"


class IncorrectTokenFormatException(NotesExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"

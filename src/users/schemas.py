"""Валидация для входа в учетную запись"""

from pydantic import BaseModel, EmailStr


class UsersAuthS(BaseModel):
    """Валидация регистарции пользователя"""

    email: EmailStr
    password: str


class Token(BaseModel):
    """Модель токена"""

    access_token: str
    token_type: str

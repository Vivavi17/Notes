"""Модуль роутера пользователей"""

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.users.schemas import Token, UsersAuthS
from src.users.service import users_service

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/register", status_code=201)
async def register(data: UsersAuthS) -> None:
    """Создание учетной записи пользователя"""

    return await users_service.register(data.email, data.password)


@users_router.post("/token")
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Token:
    """Вход пользователя по логину и паролю, пользователь получает токен доступа"""

    return await users_service.login(data.username, data.password)

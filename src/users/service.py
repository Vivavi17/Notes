"""Бизнес-логика работы пользователей"""

from pydantic import EmailStr

from src.exceptions import (IncorrectLoginOrPasswordException,
                            UserAlreadyExistsException,
                            UserDoesntExistsException)
from src.users.auth import create_access_token, get_hashed_pwd, verify_pwd
from src.users.dao import UsersDAO
from src.users.schemas import Token


class UsersService:
    """Логика работы пользователей"""

    dao = UsersDAO

    async def find_user(self, **data):
        """Найти пользователя по фильтру"""

        user = await self.dao.find_one_or_none(**data)
        if not user:
            raise UserDoesntExistsException
        return user

    async def register(self, email: EmailStr, password: str) -> None:
        """Добавить нового пользователя"""

        is_exist = await self.dao.find_one_or_none(email=email)
        if is_exist:
            raise UserAlreadyExistsException
        hashed_password = get_hashed_pwd(password)
        await self.dao.add(
            email=email,
            hashed_password=hashed_password,
        )

    async def login(self, email: EmailStr, password: str) -> Token:
        """Вход в учетную запись"""

        user = await self.find_user(email=email)
        if not verify_pwd(password, user.hashed_password):
            raise IncorrectLoginOrPasswordException

        access_token = create_access_token({"sub": str(user.id)})
        return Token(access_token=access_token, token_type="bearer")


users_service = UsersService()

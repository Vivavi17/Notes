from pydantic import EmailStr

from src.users.dao import UsersDAO
from src.users.auth import get_hashed_pwd, verify_pwd, create_access_token
from src.exceptions import UserDoesntExistsException, UserAlreadyExistsException, IncorrectLoginOrPasswordException
from src.users.schemas import Token


class UsersService:
    dao = UsersDAO

    async def find_user(self, **data):
        user = await self.dao.find_one_or_none(**data)
        if not user:
            raise UserDoesntExistsException
        return user

    async def register(self, email: EmailStr, password: str) -> None:
        is_exist = await self.dao.find_one_or_none(email=email)
        if is_exist:
            raise UserAlreadyExistsException
        hashed_password = get_hashed_pwd(password)
        await self.dao.add(
            email=email,
            hashed_password=hashed_password,
        )

    async def login(self, email: EmailStr, password: str) -> Token:
        user = await self.find_user(email=email)
        if not verify_pwd(password, user.hashed_password):
            raise IncorrectLoginOrPasswordException

        access_token = create_access_token({"sub": str(user.id)})
        return Token(access_token=access_token, token_type="bearer")


users_service = UsersService()

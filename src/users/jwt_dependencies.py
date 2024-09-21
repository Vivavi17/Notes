from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from jose import ExpiredSignatureError, jwt

from src.config import settings
from src.users.dao import UsersDAO
from src.exceptions import IncorrectTokenFormatException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/token")


async def get_curr_user(access_token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError as exp_error:
        raise IncorrectTokenFormatException from exp_error
    if not (user_id := payload.get("sub")):
        raise IncorrectTokenFormatException
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise IncorrectTokenFormatException
    return user

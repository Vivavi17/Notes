from src.base.base_dao import BaseDAO
from src.users.models import Users


class UsersDAO(BaseDAO):
    model = Users

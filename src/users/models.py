"""Модель для работы с пользователями"""

from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Users(Base): # pylint: disable=too-few-public-methods
    """Модель контекста пользователя"""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

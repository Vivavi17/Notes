from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    notes: Mapped["Notes"] = relationship("Notes", back_populates="user")
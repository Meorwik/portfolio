from sqlalchemy import String, Enum, Date, BigInteger
from sqlalchemy.orm import mapped_column, Mapped
from src.database.postgres.enums import Roles
from sqlalchemy.sql.functions import current_date
from src.database.base import Base
from typing import Final

MAX_USERNAME_LENGTH: Final[int] = 32
MAX_FIRST_NAME_LENGTH: Final[int] = 50
MAX_LAST_NAME_LENGTH: Final[int] = 50

MIN_PASSWORD_LENGTH: Final[int] = 8
MAX_PASSWORD_LENGTH: Final[int] = 16

# TODO: Provide password column with minimum string length

class User(Base):
    __tablename__: str = 'Users'

    id: Mapped[BigInteger] = mapped_column(BigInteger, primary_key=True, nullable=False, unique=True, autoincrement=True)
    username: Mapped[String] = mapped_column(String(length=MAX_USERNAME_LENGTH), nullable=True)
    password: Mapped[String] = mapped_column(String(length=MAX_PASSWORD_LENGTH), nullable=True)
    first_name: Mapped[String] = mapped_column(String(length=MAX_FIRST_NAME_LENGTH), nullable=True)
    last_name: Mapped[String] = mapped_column(String(length=MAX_LAST_NAME_LENGTH), nullable=True)
    role: Mapped[Enum] = mapped_column(Enum(Roles), default=Roles.user)
    register_date: Mapped[Date] = mapped_column(Date, default=current_date())

    def __repr__(self):
        return f"User - {self.id} Role - {self.role}"
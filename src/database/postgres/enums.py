from typing import Final
from enum import Enum


class Roles(Enum):
    user: Final[str] = "user"
    admin: Final[str] = "admin"

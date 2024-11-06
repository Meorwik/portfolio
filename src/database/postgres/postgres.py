from sqlalchemy.sql import select
from src.database.postgres.enums import Roles
from src.database.postgres.models import User
from ..base import DatabaseManager, Base
from typing import Union


class PostgresManager(DatabaseManager):

    async def init(self) -> bool:
        async with self.engine.begin() as connection:
            await connection.run_sync(Base.metadata.create_all)
        return True

    """
                        ACTIONS WITH USERS
    """

    async def add_user(self, user: User) -> bool:
        async with self.Session() as session:
            session.add(user)
            await session.commit()

        return True

    async def get_user(self, user_id: Union[str, int]) -> User:
        async with self.Session() as session:
            query = select(User).where(User.id == user_id)
            result = await session.execute(query)
            return result.scalars().one_or_none()

    async def get_admin(self) -> User:
        async with self.Session() as session:
            query = select(User).where(User.role == Roles.admin)
            result = await session.execute(query)
            return result.scalars().one()


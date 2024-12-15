from asyncio import current_task
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker, async_scoped_session
)

from src.config.database.settings import settings

class Database:

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url, echo=echo)
        self.factory = async_sessionmaker(bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False)

    def get_scope_session(self):
        return async_scoped_session(
            session_factory=self.factory,
            scopefunc=current_task
        )

    @asynccontextmanager
    async def get_db_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()

    async def get_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.factory()
        try:
            yield session
        except exc.SQLAlchemyError as e:
            print(e)
            await session.rollback()
        finally:
            await session.close()

# database = Database(settings.get_db(), settings.db_echo)
database = Database("sqlite+aiosqlite:///Database.db", True)

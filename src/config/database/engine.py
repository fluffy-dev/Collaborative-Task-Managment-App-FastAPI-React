from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker
)

from src.config.settings import settings

class Database:

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url, echo=echo)
        self.factory = async_sessionmaker(bind=self.engine, autoflush=False, auto_commit=False, expire_on_commit=False)

    async def get_session(self):
        from sqlalchemy import exc

        session: AsyncSession = self.factory()
        try:
            yield session
        except exc.SQLAlchemyError:
            await session.rollback()
        finally:
            await session.close()

database = Database(settings.get_db(), settings.db_echo)


from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from src.config.database.engine import database

Session = Annotated[AsyncSession, Depends(database.get_session())]

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import func, TIMESTAMP, FetchedValue

from datetime import datetime


class Base(DeclarativeBase):
    """
    Basic model for sqlalchemy

    id:int
    created_at: datetime
    updated_at: datetime
    """

    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True, server_default=FetchedValue())

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

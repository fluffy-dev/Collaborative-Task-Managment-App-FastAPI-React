from sqlalchemy.orm import Mapped, mapped_column
from src.lib.base_model import Base
from sqlalchemy import String

class TaskModel(Base):

    __tablename__ = "Task"

    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(500))

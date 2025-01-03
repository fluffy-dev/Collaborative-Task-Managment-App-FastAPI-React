from src.app.task.models.task import TaskModel
from src.lib.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from typing import List

class UserModel(Base):

    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str]

    tasks: Mapped[List["TaskModel"]] = relationship("TaskModel", backref="task", cascade="all, delete-orphan")

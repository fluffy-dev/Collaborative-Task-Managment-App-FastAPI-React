from sqlalchemy.orm import Mapped, mapped_column
from src.lib.base_model import Base
from sqlalchemy import String, ForeignKey

class TaskModel(Base):

    __tablename__ = "task"

    title: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(500))
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "user.id",
        ondelete="CASCADE",
    ), nullable=False)
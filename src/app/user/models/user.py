from src.lib.base_model import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class UserModel(Base):

    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str]
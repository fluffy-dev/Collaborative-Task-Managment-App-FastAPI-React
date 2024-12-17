from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from src.lib.base_model import Base

class PermissionModel(Base):
    __tablename__ = "permission"

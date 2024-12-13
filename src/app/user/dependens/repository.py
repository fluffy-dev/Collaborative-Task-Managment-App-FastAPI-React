from fastapi import Depends
from typing import Annotated
from src.app.user.repository.user import UserRepository

IUserRepository = Annotated[UserRepository, Depends()]
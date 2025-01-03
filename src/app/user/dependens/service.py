from fastapi import Depends
from typing import Annotated
from src.app.user.service import UserService

IUserService = Annotated[UserService, Depends()]

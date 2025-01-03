from typing import Annotated
from fastapi import Depends

from src.api.user.router import current_user

IUser = Annotated[current_user, Depends()]
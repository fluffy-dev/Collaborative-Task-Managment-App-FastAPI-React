from typing import Annotated
from fastapi import Depends
from src.app.auth.service import AuthService

IAuthService = Annotated[AuthService, Depends()]
from fastapi import Depends
from typing import Annotated
from src.app.auth.token_service import TokenService

ITokenService = Annotated[TokenService, Depends()]
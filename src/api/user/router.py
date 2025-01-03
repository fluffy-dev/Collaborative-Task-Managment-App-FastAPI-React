from fastapi import APIRouter
from typing import List

from src.app.user.dto import UserDTO
from src.app.user.dependens.service import IUserService


router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=UserDTO)
async def current_user(service: IUserService, token: str| None = None):
    return await service.get_me(token)

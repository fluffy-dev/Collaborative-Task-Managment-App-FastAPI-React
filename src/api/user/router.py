from fastapi import APIRouter
from typing import List

from src.app.user.dto import RegistrationDTO, UserDTO
from src.app.user.dependens.service import IUserService


router = APIRouter(prefix="/user", tags=["user"])

@router.get("/", response_model=UserDTO)
async def current_user(service: IUserService, token: str| None = None):
    return await service.get_me(token)

@router.post("/", response_model=UserDTO)
async def add_user(service: IUserService, dto: RegistrationDTO):
    return await service.add(dto)

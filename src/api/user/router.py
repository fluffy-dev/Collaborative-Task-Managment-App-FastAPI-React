from fastapi import APIRouter
from typing import List

from src.app.user.dto import RegistrationDTO, UserDTO
from src.app.user.dependens.service import IUserService


router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{pk}")
async def get(service: IUserService, pk: int):
    return await service.get(pk)

@router.get("/", response_model=List[UserDTO])
async def get_list(service: IUserService, limit:int):
    return await service.get_list(limit)

@router.post("/", response_model=RegistrationDTO)
async def add(service: IUserService, dto: RegistrationDTO):
    return await service.add(dto)

@router.post("/{pk}", response_model=UserDTO)
async def edit(service: IUserService, dto: RegistrationDTO, pk:int):
    return await service.edit(dto, pk)

@router.delete("/{pk}")
async def remove(service: IUserService, pk:int):
    return await service.remove(pk)


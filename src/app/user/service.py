from src.app.user.dependens.repository import IUserRepository
from src.app.user.dto import UserDTO, FindUserDTO
from src.app.user.entity import UserEntity
from src.app.auth.dependens.token_service import ITokenService

from fastapi import HTTPException, status

class UserService:
    def __init__(self, repository: IUserRepository, token_service: ITokenService):
        self.repository = repository
        self.token_service = token_service

    async def add(self, dto: UserEntity):
        return await self.repository.create(dto)

    async def get_me(self, token: str):
        data = await self.token_service.decode_token(token)
        user_email = data.get("user").get("email")
        if not user_email:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
        return await self.get_user(FindUserDTO(email=data["user"]["email"]))

    async def get_user(self, dto) -> UserDTO:
        user = await self.repository.get_user(FindUserDTO(email=dto.email))
        return user

    async def get_list(self, limit:int):
        return await self.repository.get_list(limit)

    async def edit(self, dto: UserDTO, pk: int):
        return await self.repository.update(dto, pk)

    async def remove(self, pk: int):
        return await self.repository.delete(pk)
    


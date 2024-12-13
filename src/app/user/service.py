from src.app.user.dependens.repository import IUserRepository
from src.app.user.dto import RegistrationDTO, UserDTO
from src.app.user.entity import UserEntity


class UserService:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def add(self, dto: RegistrationDTO):
        user_entity = UserEntity(**dto.model_dump())
        return await self.repository.create(user_entity)

    async def get(self, pk:int):
        return await self.repository.get(pk)

    async def get_list(self, limit:int):
        return await self.repository.get_list(limit)

    async def edit(self, dto: UserDTO, pk: int):
        return await self.repository.update(dto, pk)

    async def remove(self, pk: int):
        return await self.repository.delete(pk)
    


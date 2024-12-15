from src.app.user.dependens.repository import IUserRepository
from src.app.user.dto import RegistrationDTO, UserDTO, FindUserDTO
from src.app.user.entity import UserEntity
from src.app.auth.dependens.token_service import ITokenService


class UserService:
    def __init__(self, repository: IUserRepository, token_service: ITokenService):
        self.repository = repository
        self.token_service = token_service

    async def add(self, dto: RegistrationDTO):
        registration_data = dto.model_dump()
        registration_data.pop("password2")
        user_entity = UserEntity(**registration_data)
        return await self.repository.create(user_entity)

    async def get_me(self, token: str):
        data = await self.token_service.decode_token(token)
        return await self.repository.get_user(FindUserDTO(email=data["user"]["email"]))

    async def get_user(self, dto):
        user = await self.repository.get_user(FindUserDTO(email=dto.email))
        return user

    async def get_list(self, limit:int):
        return await self.repository.get_list(limit)

    async def edit(self, dto: UserDTO, pk: int):
        return await self.repository.update(dto, pk)

    async def remove(self, pk: int):
        return await self.repository.delete(pk)
    


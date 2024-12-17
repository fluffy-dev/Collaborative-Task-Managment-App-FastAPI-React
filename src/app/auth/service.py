from src.app.user.dto import LoginDTO, RegistrationDTO
from src.app.user.dependens.service import IUserService
from src.app.auth.dependens.token_service import ITokenService
from src.app.user.entity import UserEntity
from src.lib.exceptions import AlreadyExistError, RegistrationError


class AuthService:
    def __init__(self, user_service: IUserService, token_service: ITokenService):
        self.user_service = user_service
        self.token_service = token_service

    async def registration(self, dto: RegistrationDTO):
        registration_data = dto.model_dump()
        registration_data.pop('password2')
        user_entity = UserEntity(**registration_data)
        try:
            return await self.user_service.add(user_entity)
        except AlreadyExistError as e:
            raise RegistrationError(e)


    async def login(self, dto: LoginDTO):
        user = await self.user_service.get_user(dto)
        if not user:
            raise ValueError("invalid login or password")

        verify = UserEntity.verify(dto.password, user.password)
        if verify:
            return await self.token_service.get_token(dto)

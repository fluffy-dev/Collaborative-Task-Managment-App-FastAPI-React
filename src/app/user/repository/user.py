from src.config.database.session import Session
from src.app.user.models.user import UserModel
from src.app.user.entity import UserEntity
from src.app.user.dto import UserDTO, LoginDTO, FindUserDTO
from src.lib.exceptions import AlreadyExistError

from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, delete, Null

class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    async def create(self, user: UserEntity):
        instance = UserModel(**user.__dict__)
        self.session.add(instance)
        try:
            await self.session.commit()
        except IntegrityError:
            raise AlreadyExistError(f"{instance.email} is already exist")

        await self.session.refresh(instance)
        return self._get_dto(instance)

    async def get(self, pk: int):
        stmt = select(UserModel).filter_by(id=pk)
        raw = await self.session.execute(stmt)
        result = raw.scalar_one_or_none()
        return self._get_dto(result) if result else None

    async def get_user(self, dto: FindUserDTO):
        stmt = select(UserModel).filter_by(**dto.model_dump(exclude_none=True))
        raw = await self.session.execute(stmt)
        result = raw.scalar_one_or_none()
        return self._get_dto(result) if result else None

    async def get_list(self, limit: int):
        stmt = select(UserModel).limit(limit)
        raw = await self.session.execute(stmt)
        users = [self._get_dto(user).__dict__ for user in raw.scalars().all()]
        return users

    async def update(self, dto: UserDTO, pk: int):
        stmt = update(UserModel).values(**dto.model_dump()).filter_by(id=pk).returning(UserModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        return self._get_dto(raw.scalar_one())

    async def delete(self, pk:int):
        stmt = delete(UserModel).where(UserModel.id==pk)
        await self.session.execute(stmt)
        await self.session.commit()

    def _get_dto(self, row:UserModel) -> UserDTO:
        return UserDTO(
            id=row.id,
            email=row.email,
            password=row.password,
        )


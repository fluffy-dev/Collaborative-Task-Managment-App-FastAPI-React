from src.app.task.dto import TaskDTO
from src.config.database.session import Session
from src.app.task.models.Task import TaskModel
from src.app.task.entity import TaskEntity

from sqlalchemy import select, update, delete


class TaskRepository:
    """
    class for work with Task model

    create:
    :param task: TaskEntity
    :return TaskDTO

    get:
    :param pk: int
    :return TaskDTO

    get_list:
    :param limit
    :return List[TaskDTO]

    update:
    :param TaskDTO, pk
    :return TaskDTO

    delete:
    :param pk
    :return None

    """
    def __init__(self, session: Session):
        self.session = session

    async def create(self, task: TaskEntity):
        instance = TaskModel(**task.__dict__)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return self._get_dto(instance)

    async def get(self, pk: int):
        stmt = select(TaskModel).where(TaskModel.id == pk)
        raw = await self.session.execute(stmt)
        result = raw.scalar_one_or_none()
        return self._get_dto(result) if result else None

    async def get_list(self, limit:int):
        stmt = select(TaskModel).limit(limit)
        raw = await self.session.execute(stmt)
        tasks_list = [self._get_dto(task).__dict__ for task in raw.scalars().all()]
        return tasks_list

    async def update(self, dto: TaskDTO, pk:int):
        dto.id = pk
        stmt = update(TaskModel).values(**dto.model_dump()).filter_by(id=pk).returning(TaskModel)
        raw = await self.session.execute(stmt)
        await self.session.commit()
        result = raw.scalar_one()
        return self._get_dto(result)

    async def delete(self, pk:int):
        stmt = delete(TaskModel).where(TaskModel.id == pk)
        await self.session.execute(stmt)
        await self.session.commit()

    def _get_dto(self, row: TaskModel):
            return TaskDTO(
                id = row.id,
                title=row.title,
                description=row.description
            )


    
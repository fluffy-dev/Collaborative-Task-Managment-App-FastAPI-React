from src.app.task.dependens.repository import ITaskRepository
from src.app.task.dto import TaskDTO, AddTaskDTO
from src.app.task.entity import TaskEntity

class TaskService:
    """

    service to work with Tasks

    init: Repository

    functions:

    get params: id: int
    get output: TaskDTO

    get_list params: limit:int
    get_list output: List[TaskDTO]

    add params: dto: TaskDTO
    output params: TaskDTO

    update params: dto: TaskDTO; id: int
    update output: TaskDTO

    delete params: id: int
    delete output: TaskDTO

    """

    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    async def get(self, pk):
        return await self.repository.get(pk)

    async def get_list(self, limit: int):
        return await self.repository.get_list(limit)

    async def add(self, dto: AddTaskDTO):
        task_entity = TaskEntity(**dto.model_dump())
        return await self.repository.create(task_entity)

    async def edit(self, dto: TaskDTO, pk: int):
        return await self.repository.update(dto, pk)

    async def remove(self, pk: int):
        return await self.repository.delete(pk)

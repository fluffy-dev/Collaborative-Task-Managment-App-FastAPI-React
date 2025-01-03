from fastapi import APIRouter
from typing import List

from src.app.task.dependens.service import ITaskService
from src.app.task.dto import TaskDTO, AddTaskDTO
from src.api.user.depends import IUser

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/", response_model=List[TaskDTO])
async def get_tasks_list(service: ITaskService, limit: int, user:IUser):
    return await service.get_list(limit, user)


@router.post("/add", response_model=TaskDTO)
async def add_task(dto: AddTaskDTO, service: ITaskService,  user:IUser):
    return await service.add(dto)

@router.get("/{pk}", response_model=TaskDTO)
async def get_task(service: ITaskService, pk: int):
    return await service.get(pk)

@router.post("/{pk}", response_model=TaskDTO)
async def edit_task(service: ITaskService, dto: TaskDTO, pk: int):
    return await service.edit(dto, pk)

@router.delete("/{pk}")
async def delete_task(service: ITaskService, pk: int):
    return await service.remove(pk)
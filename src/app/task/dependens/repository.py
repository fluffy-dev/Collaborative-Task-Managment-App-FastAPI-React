from fastapi import Depends
from typing import Annotated
from src.app.task.repository.task import TaskRepository

ITaskRepository = Annotated[TaskRepository, Depends()]
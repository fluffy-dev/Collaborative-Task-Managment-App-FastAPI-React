from fastapi import Depends
from typing import Annotated
from src.app.task.service import TaskService

ITaskService = Annotated[TaskService, Depends()]

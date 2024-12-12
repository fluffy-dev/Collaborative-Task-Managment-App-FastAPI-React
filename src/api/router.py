from fastapi import APIRouter
from src.api.task.router import router as task_router

router = APIRouter(prefix="/api", tags=["api"])

router.include_router(task_router)

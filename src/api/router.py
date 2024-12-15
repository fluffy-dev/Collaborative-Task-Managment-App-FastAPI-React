from fastapi import APIRouter

from src.api.task.router import router as task_router
from src.api.user.router import router as user_router
from src.api.auth.router import router as auth_router
router = APIRouter(prefix="/api", tags=["api"])

router.include_router(task_router)
router.include_router(user_router)
router.include_router(auth_router)
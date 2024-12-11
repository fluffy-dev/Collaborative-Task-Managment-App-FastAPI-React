from src.config.database.session import Session

class TaskRepository:

    def __init__(self, session: Session):
        self.session = session

    async def add_task(self):
        pass
    
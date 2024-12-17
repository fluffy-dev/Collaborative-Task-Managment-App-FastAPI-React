from pydantic import BaseModel, constr

class TaskDTO(BaseModel):
    id: int = None
    title: constr(max_length=30) = None
    description: constr(max_length=500) = None

class AddTaskDTO(BaseModel):
    title: constr(max_length=30) = None
    description: constr(max_length=500) = None
    user_id: int
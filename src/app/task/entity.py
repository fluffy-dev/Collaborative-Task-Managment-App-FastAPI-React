from dataclasses import dataclass


@dataclass
class TaskEntity:
    title:str
    description:str
    user_id: int

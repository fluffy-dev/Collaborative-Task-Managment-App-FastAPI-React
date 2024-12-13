from dataclasses import dataclass

@dataclass
class UserEntity:
    email: str
    password: str

    def __post_init__(self):
        pass
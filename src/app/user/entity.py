from dataclasses import dataclass
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@dataclass
class UserEntity:
    email: str
    password: str|None = None

    def __post_init__(self):
        self.password = pwd_context.hash(self.password)

    @staticmethod
    def verify(password, hashed_password):
        return pwd_context.verify(password, hashed_password)



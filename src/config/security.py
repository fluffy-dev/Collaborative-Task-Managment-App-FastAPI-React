from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    secret_key: str = Field(..., alias="SECRET_KEY")
    access_token_expire_minutes: int = Field(..., alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    algorithm: str = Field("HS256", alias="SECRET_KEY_ALGORITHM")


settings = Settings()

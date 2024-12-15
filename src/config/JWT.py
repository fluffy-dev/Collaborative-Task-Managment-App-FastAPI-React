from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    ACCESS_TOKEN_LIFETIME: int = Field(3600, alias="ACCESS_TOKEN_LIFETIME")


settings = Settings()

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    db_url_scheme: str = Field("sqlite+aiosqlite", alias="DB_URL_SCHEME")
    db_filename: str = Field("Database.db", alias="DB_FILENAME")
    db_echo: bool = Field(False, alias="DB_ECHO")

    def get_db(self) -> str:
        return f"{self.db_url_scheme}:///{self.db_filename}"


settings = Settings()

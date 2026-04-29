from pydantic_settings import BaseSettings

class DatabaseSettings(BaseSettings):
    DB_URL: str

    class Config():
        env_file = ".env"

database_settings = DatabaseSettings()
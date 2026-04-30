from pydantic_settings import BaseSettings

# Database Config:
class DatabaseSettings(BaseSettings):
    DB_URL: str

    class Config():
        env_file = ".env"

database_settings = DatabaseSettings()

# JWT Config:
class JWTSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str

    class Config():
        env_file = ".env"

jwt_settings = JWTSettings()
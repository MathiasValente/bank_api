from pydantic_settings import BaseSettings

# Database Config:
class EnvVars(BaseSettings):
    DB_URL: str
    SECRET_KEY: str
    ALGORITHM: str

    class Config():
        env_file = ".env"

env_vars = EnvVars()
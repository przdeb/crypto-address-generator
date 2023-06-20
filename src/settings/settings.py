from pydantic import BaseSettings

from src.settings import PROJECT_ROOT


class Settings(BaseSettings):
    app_name: str = "Zeply interview"
    database_url = f"sqlite:///{PROJECT_ROOT}/database.db"
    private_key: str

    class Config:
        env_file = ".env"


settings = Settings()

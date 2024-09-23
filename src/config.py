"""Конфигурация переменных среды"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Базовый класс настроек переменных среды"""
    UVICORN_HOST: str
    UVICORN_PORT: int

    PG_HOST: str
    PG_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    URL_YA_SPELLER_JSON: str

    @property
    def DATABASE_URL(self): # pylint: disable=invalid-name
        """Создание URL подключения к БД"""
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.POSTGRES_DB}" # pylint: disable=line-too-long

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

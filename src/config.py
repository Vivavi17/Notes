from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    UVICORN_HOST: str
    UVICORN_PORT: int

    PG_HOST: str
    PG_PORT: int
    PG_USERNAME: str
    PG_PASSWORD: str
    PG_DATABASE: str

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.PG_USERNAME}:{self.PG_PASSWORD}@{self.PG_HOST}:{self.PG_PORT}/{self.PG_DATABASE}"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="APP_")

settings = Settings()

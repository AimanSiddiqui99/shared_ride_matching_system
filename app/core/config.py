from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Ride Matching System"

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    REDIS_URL: str

    class Config:
        env_file = ".env"


settings = Settings()

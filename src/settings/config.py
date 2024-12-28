import os
from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    DEBUG: str

    # Database
    POSTGRES_DRIVER: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return f"{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def FASTAPI_SETTINGS(self) -> dict[str, str | int | bool | dict]:
        return {
            "docs_url": "/docs",
            "redoc_url": "/",
            "debug": self.DEBUG,
        }

    CORS_ALLOWED_ORIGINS: List[str]

    COOKIE_MAX_AGE: int = 3600

    # jwt secret and algorithm
    JWT_SECRET: str
    JWT_ALGORITHM: str

    # hashing parameters
    CRYPTOGRAPHIC_HASH_FUNCTION: str = "sha256"
    PWD_HASH_SALT: bytes = os.urandom(16)
    PWD_HASH_ITERATIONS: int = 100_000
    DK_LEN: int = 32

    class Config:
        env_file = ".env"


settings = Settings()

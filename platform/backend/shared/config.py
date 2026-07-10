from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Unified Platform API"
    app_version: str = "0.1.0"
    database_url: str = "postgresql+psycopg://platform:platform@localhost:5432/platform"
    redis_url: str = "redis://localhost:6379/0"
    rabbitmq_url: str = "amqp://platform:platform@localhost:5672/"
    qdrant_url: str = "http://localhost:6333"
    minio_endpoint: str = "localhost:9000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    return Settings()

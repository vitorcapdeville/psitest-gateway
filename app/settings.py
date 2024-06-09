from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PSITEST_AUTH: str
    PSITEST_CADASTRO: str
    PSITEST_QUESTIONARIOS: str

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()

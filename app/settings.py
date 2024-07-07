from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PSITEST_AUTH: str
    PSITEST_CADASTRO: str
    PSITEST_QUESTIONARIOS: str
    PSITEST_RESPOSTAS: str


@lru_cache
def get_settings():
    return Settings()

import os

from pydantic import PostgresDsn


POSTGRES_USER: str = os.getenv("POSTGRES_USER", default="postgres")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", default="postgres")
DB_HOST: str = os.getenv("DB_HOST", default="0.0.0.0")
DB_PORT: int = os.getenv("DB_PORT", default=5432)
DB_NAME: str = os.getenv("POSTGRES_DB", default="db")

DATABASE_ASYNC_URL: PostgresDsn = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_SYNC_URL: PostgresDsn = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

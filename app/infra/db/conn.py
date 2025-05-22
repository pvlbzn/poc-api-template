import logging
from typing import Optional

import asyncpg

from app.config import Settings

log: logging.Logger = logging.getLogger(__name__)
_connection: Optional[asyncpg.Pool] = None


async def connect(settings: Settings = Settings()):
    global _connection
    _connection = await asyncpg.create_pool(
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        database=settings.DB_NAME,
    )
    log.info("Connected to database")


async def close():
    global _connection
    if _connection:
        await _connection.close()
    log.info("Database connection closed")


def get_pool() -> asyncpg.Pool:
    if not _connection:
        raise RuntimeError("Database pool is not initialized")
    return _connection

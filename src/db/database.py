from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from src.settings import app_settings

Base = declarative_base()

connection_string = app_settings
async_engine = create_async_engine(
    connection_string.DB_URI,
    pool_pre_ping=True,
    future=True,
)
async_factory = async_sessionmaker(
    bind=async_engine,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession, 
)


async def async_get_session() -> AsyncGenerator[
    AsyncSession, None
]:  # noqa: WPS430, WPS442
    async with async_factory() as session:
        yield session


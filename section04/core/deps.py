from typing import Generator

from core.database import Session
from sqlalchemy.ext.asyncio import AsyncSession


async def get_session() -> Generator:  # type: ignore
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()

"""Authentication settings for the FastAPI Users package."""

from typing import Annotated

from fastapi import Depends
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db import get_async_session
from src.models import User
from src.settings.config import settings

cookie_transport = CookieTransport(
    cookie_max_age=3600, cookie_name="stockticcookie"
)


def get_jwt_strategy() -> JWTStrategy:
    """Get the JWT (JSON Web Token) authentication strategy.

    Returns:
        JWTStrategy: The JWT authentication strategy.
    """
    return JWTStrategy(secret=settings.JWT_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)


async def get_user_table(
    session: Annotated[AsyncSession, Depends(get_async_session)]
):
    """Get the SQLAlchemyUserDatabase instance for the User model.

    Args:
        session (AsyncSession): The asynchronous database session.

    Yields:
        SQLAlchemyUserDatabase: The SQLAlchemyUserDatabase instance.
    """
    yield SQLAlchemyUserDatabase(session, User)

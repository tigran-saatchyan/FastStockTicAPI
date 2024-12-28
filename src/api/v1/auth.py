from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.models import User
from src.schemas.users import UserRead, UserCreate, UserUpdate
from src.services.managers import get_user_manager
from src.settings.auth import auth_backend

PREFIX = "/api/v1"
AUTH_TAG = "Authentication"

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


def set_up_auth_routes(application: FastAPI):
    """Set up authentication routes for the FastAPI application.

    Args:
        application (FastAPI): The FastAPI application instance.
    """
    application.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix=f"{PREFIX}/jwt",
        tags=[AUTH_TAG],
    )
    application.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix=PREFIX,
        tags=[AUTH_TAG],
    )
    application.include_router(
        fastapi_users.get_users_router(UserRead, UserUpdate),
        prefix="/users",
        tags=["Users"],
    )

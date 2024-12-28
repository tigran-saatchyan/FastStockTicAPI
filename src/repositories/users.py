"""Repository for interacting with the User model in the database."""

from src.models import User
from src.repositories.base_repository import BaseRepository


class UsersRepository(BaseRepository):
    """Repository for interacting with the User model in the database.

    Attributes:
        model: The User model.
        session: The database session.
    """

    model = User

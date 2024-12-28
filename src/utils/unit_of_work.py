"""Unit of Work pattern implementation."""

from abc import ABC, abstractmethod
from typing import Type

from src.db import async_session_maker
from src.repositories.users import UsersRepository


class IUnitOfWork(ABC):
    users: Type[UsersRepository]

    @abstractmethod
    def __init__(self):
        """Initialize the Unit of Work."""
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        """Enter the asynchronous context."""
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        """Exit the asynchronous context."""
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        """Commit changes made during the Unit of Work."""
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        """Rollback changes made during the Unit of Work."""
        raise NotImplementedError


class UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        """Enter the asynchronous context, creating repositories."""
        self.session = self.session_factory()
        self.users = UsersRepository(self.session)

    async def __aexit__(self, *args):
        """Exit the asynchronous context, rolling back changes and
        closing the session.
        """
        await self.rollback()
        await self.session.close()

    async def commit(self):
        """Commit changes made during the Unit of Work."""
        await self.session.commit()

    async def rollback(self):
        """Rollback changes made during the Unit of Work."""
        await self.session.rollback()

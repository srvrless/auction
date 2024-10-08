from abc import ABC, abstractmethod
from typing import Type

from src.repositories.auth import AuthRepository
from src.db.database import async_factory
from src.repositories.lots import LotsRepository
from src.repositories.users import UsersRepository


class InterfaceUnitOfWork(ABC):
    lots: Type[LotsRepository]
    auth: Type[AuthRepository]
    users: Type[UsersRepository]

    @abstractmethod
    def __init__(self): ...

    @abstractmethod
    async def __aenter__(self): ...

    @abstractmethod
    async def __aexit__(self, *args): ...

    @abstractmethod
    async def commit(self): ...

    @abstractmethod
    async def rollback(self): ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_factory

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.lots = LotsRepository(self.session)
        self.auth = AuthRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

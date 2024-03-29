from abc import ABC, abstractmethod
from uuid import UUID

from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, id: UUID, data: dict) -> int:
        stmt = (
            update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_all(self):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def find_one(self, filter_by):
        filter_conditions = {"id": filter_by["id"]}
        stmt = select(self.model).filter_by(**filter_conditions)
        res = await self.session.execute(stmt)
        res = res.scalar_one().to_read_model()
        return res

    async def delete_one(self, id: UUID):
        stmt = delete(self.model).where(self.model.id == id).returning(self.model.id)
        row = await self.session.execute(stmt)
        result = row.fetchone()
        if result is not None:
            return result[0]

from src.database import async_session
from sqlalchemy import select, insert

class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, limit=None, offset=None, order_by=None, **filter_by):
        async with async_session() as session:
            query = select(cls.model.__table__).filter_by(**filter_by).order_by(order_by).offset(offset).limit(limit)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()

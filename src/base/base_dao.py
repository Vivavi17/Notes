"""Модуль с родительским классом ДАО"""

from sqlalchemy import insert, select

from src.database import async_session


class BaseDAO:
    """Базовый интерфейс CRUD"""

    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """Поиск единственной записи"""
        async with async_session() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, limit=None, offset=None, order_by=None, **filter_by):
        """Получение статей с фильтрацией и пагинацией"""
        async with async_session() as session:
            query = (
                select(cls.model.__table__)
                .filter_by(**filter_by)
                .order_by(order_by)
                .offset(offset)
                .limit(limit)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        """Добавление записи в таблицу"""
        async with async_session() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()

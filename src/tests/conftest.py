"""Конфигурация тестов"""

import pytest
from fastapi.testclient import TestClient
from mock import Mock

from src.main import app
from src.users.auth import get_hashed_pwd
from src.users.jwt_dependencies import get_curr_user


@pytest.fixture(scope="session")
def users():
    """Возвращает список пользователей"""
    list_users = {
        "first@test.com": Mock(
            id=1, email="first@test.com", hashed_password=get_hashed_pwd("Test")
        )
    }
    return list_users


def new_dependence(q: str | None = None):  # pylint: disable=unused-argument
    """Переопределение зависимости"""
    return Mock(id=1, email="first@test.com", hashed_password=get_hashed_pwd("Test"))


app.dependency_overrides[get_curr_user] = new_dependence


@pytest.fixture
def client():
    """Создание тестового клиента"""
    with TestClient(app) as _client:
        yield _client

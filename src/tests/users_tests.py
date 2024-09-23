"""Тестировние логики работы пользователей"""

import pytest
from mock import Mock

from src.users.auth import get_hashed_pwd


@pytest.mark.parametrize(
    "email,password,status",
    [
        ("first@test.com", "Test", 409),
        ("second@test.com", "Test", 201),
        ("nomail", "Test", 422),
    ],
)
async def test_register_user(email, password, status, client, mocker, users):
    """Тестирование регистрации пользователей"""
    user = Mock(id=1, email=email, hashed_password=get_hashed_pwd(password))
    mocker.patch(
        "src.base.base_dao.BaseDAO.find_one_or_none", return_value=email in users
    )
    mocker.patch("src.base.base_dao.BaseDAO.add", return_value=users.get(email, user))

    response = client.post(
        "/users/register",
        json={"email": email, "password": password, "grant_type": "password"},
    )

    assert response.status_code == status


@pytest.mark.parametrize(
    "email,password,status",
    [
        ("first@test.com", "Test", 200),
        ("first@test.com", "wrong_Test", 401),
        ("second@test.com", "Test", 401),
    ],
)
async def test_login_user(email, password, status, client, mocker, users):
    """Тестирование аутентификации пользователя"""

    mocker.patch(
        "src.base.base_dao.BaseDAO.find_one_or_none", return_value=users.get(email)
    )

    response = client.post(
        "/users/token",
        data={"username": email, "password": password, "grant_type": "password"},
        headers={"content-type": "application/x-www-form-urlencoded"},
    )

    assert response.status_code == status
    if status == 200:
        assert "access_token" in response.json()

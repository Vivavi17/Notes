"""Тестировние логики работы заметок"""

from datetime import datetime

import pytest

from src.config import settings


@pytest.mark.parametrize("body", ["My small text", "A" * 10_000])
async def test_add_note(body, client, mocker, requests_mock):
    """Тестирование добавления заметок"""

    async def add(author_id, body):  # pylint: disable=unused-argument
        return {"body": body, "created_at": datetime.now()}

    requests_mock.get(settings.URL_YA_SPELLER_JSON, status_code=200, json=[])
    mocker.patch("src.base.base_dao.BaseDAO.add", add)

    response = client.post("/notes/", json={"body": body})
    assert body == response.json()["body"]


@pytest.mark.parametrize(
    "notes", [[], [{"body": "text", "created_at": datetime.now()}]]
)
async def test_get_note(notes, client, mocker):
    """Тестирование получения заметок"""

    mocker.patch("src.base.base_dao.BaseDAO.find_all", return_value=notes)

    response = client.get("/notes/")
    assert len(notes) == len(response.json())

import pytest
from typing import Generator

from program_files.infrastructure.llm.cost.base import UsageDB
from program_files.infrastructure.llm.cost.usage_db import SQliteUsageDB

from program_files.app.context import AppContext
from program_files.shared.schemas import Usage


#===============Fixture=============================

@pytest.fixture(params=[
    SQliteUsageDB,
])
def usage_db(request) -> Generator[UsageDB, None, None]:

    db = request.param(
        app_context=AppContext(user_id="test_user"),
        db_path=":memory:"
    )

    yield db

    db.close()


#================Tests=================================

def test_get_status_returns_none_if_empty(
    usage_db: UsageDB
):
    assert usage_db.get_status() is None


def test_set_available_cost(
    usage_db: UsageDB
):
    usage_db.set_available_cost(100)

    status = usage_db.get_status()

    assert status is not None

    assert status["user_id"] == "test_user"
    assert status["total_input_tokens"] == 0
    assert status["total_output_tokens"] == 0
    assert status["total_cost"] == 0
    assert status["available_cost"] == 100


def test_write_log_and_status(
    usage_db: UsageDB,
    monkeypatch
):
    monkeypatch.setattr(
        "program_files.infrastructure.llm.cost.sqlite_db.calc_cost",
        lambda *_: 1.5
    )

    usage_db.set_available_cost(100)

    usage = Usage(
        model_name="fake-model",
        input_tokens=10,
        output_tokens=20,
    )

    usage_db.write_log_and_status(usage)

    status = usage_db.get_status()

    assert status is not None

    assert status["user_id"] == "test_user"
    assert status["total_input_tokens"] == 10
    assert status["total_output_tokens"] == 20
    assert status["total_cost"] == 1.5
    assert status["available_cost"] == 100


def test_write_log_accumulates(
    usage_db: UsageDB,
    monkeypatch
):
    monkeypatch.setattr(
        "program_files.infrastructure.llm.cost.sqlite_db.calc_cost",
        lambda *_: 1.5
    )

    usage_db.set_available_cost(100)

    usage1 = Usage(
        model_name="fake-model",
        input_tokens=10,
        output_tokens=20,
    )

    usage2 = Usage(
        model_name="fake-model",
        input_tokens=30,
        output_tokens=40,
    )

    usage_db.write_log_and_status(usage1)
    usage_db.write_log_and_status(usage2)

    status = usage_db.get_status()

    assert status is not None

    assert status["total_input_tokens"] == 40
    assert status["total_output_tokens"] == 60
    assert status["total_cost"] == 3.0
    assert status["available_cost"] == 100

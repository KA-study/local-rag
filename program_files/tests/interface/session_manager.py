import pytest

from interface.session_manager.base import SessionManagerInterface
from interface.session_manager.cli import CliSessionManagerInterface
from shared.schemas import ExitCommandError


# ====== SessionManagerInterface.select_session_id() ======

def test_select_session_id_by_index(monkeypatch):

    session_manager: SessionManagerInterface = CliSessionManagerInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "0"
    )

    result = session_manager.select_session_id(
        ["session1", "session2"]
    )

    assert result == "session1"


def test_select_session_id_by_name(monkeypatch):

    session_manager: SessionManagerInterface = CliSessionManagerInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "session2"
    )

    result = session_manager.select_session_id(
        ["session1", "session2"]
    )

    assert result == "session2"


def test_select_session_id_new_session(monkeypatch):

    session_manager: SessionManagerInterface = CliSessionManagerInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "n"
    )

    result = session_manager.select_session_id(
        ["session1", "session2"]
    )

    assert result == "_NEW_"


def test_select_session_id_exit_command(monkeypatch):

    session_manager: SessionManagerInterface = CliSessionManagerInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: ":q"
    )

    with pytest.raises(ExitCommandError):
        session_manager.select_session_id(
            ["session1", "session2"]
        )



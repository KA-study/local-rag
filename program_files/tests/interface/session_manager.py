import pytest

from program_files.interface.session_manager.base import SessionManagerInterface
from program_files.interface.session_manager.cli import CliSessionManagerInterface
from program_files.shared.schemas import ExitCommandError


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


# ====== SessionManagerInterface.create_session_id() ======

def test_create_session_id(monkeypatch):

    session_manager: SessionManagerInterface = CliSessionManagerInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "test_session"
    )

    result = session_manager.create_session_id()

    assert result.startswith("test_session")


def test_create_session_id_exit_command(monkeypatch):

    session_manager: SessionManagerInterface = CliSessionManagerInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: ":q"
    )

    with pytest.raises(ExitCommandError):
        session_manager.create_session_id()

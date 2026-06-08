import pytest

from interface.chat.base import ChatInterface
from interface.chat.cli import CliChatInterface
from shared.schemas import ExitCommandError


def test_get_input(monkeypatch):

    chat_interface: ChatInterface = CliChatInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "hello"
    )

    result = chat_interface.get_input()

    assert result == "hello"


def test_get_input_exit_command(monkeypatch):

    chat_interface: ChatInterface = CliChatInterface()

    monkeypatch.setattr(
        "builtins.input",
        lambda _: ":q"
    )

    with pytest.raises(ExitCommandError):
        chat_interface.get_input()

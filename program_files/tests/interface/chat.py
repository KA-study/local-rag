import pytest

from interface.chat.base import ChatInterface
from interface.chat.cli import CliChatInterface
from shared.schemas import ExitCommandError

#======ChatInterface.get_input()==============
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


#===========ChatInterface.display_message()=============
def test_display_message(capsys):

    interface = CliChatInterface()

    interface.display_message(
        "assistant",
        "hello"
    )

    captured = capsys.readouterr()

    assert captured.out == "assistant: hello\n\n"

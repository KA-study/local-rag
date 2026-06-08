import pytest

from program_files.interface.chat.base import ChatInterface
from program_files.interface.chat.cli import CliChatInterface
from program_files.shared.schemas import ExitCommandError

#現時点の書き方は、GUIには対応していない（GUIはinput()によって作動するわけではないため。)
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

    chat_interface = CliChatInterface()

    chat_interface.display_message(
        "assistant",
        "hello"
    )

    captured = capsys.readouterr()

    assert captured.out == "assistant: hello\n\n"

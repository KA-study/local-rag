from dataclasses import dataclass

from program_files.interface.chat.cli import CliChatInterface
from program_files.interface.session_manager.cli import CliSessionManagerInterface
from program_files.interface.edit_tree.cli import CliEditTreeInterface
from program_files.interface.profile_run.cli import CliProfileRunInterface
from program_files.interface.switch_user_interface.cli import CliSwitchUserInterface
from program_files.interface.main.cli import CliMainInterface

@dataclass
class Cli:
    chat: type[CliChatInterface] = CliChatInterface
    session_manager: type[CliSessionManagerInterface] = CliSessionManagerInterface
    edit_tree: type[CliEditTreeInterface] = CliEditTreeInterface
    profile_run: type[CliProfileRunInterface] = CliProfileRunInterface
    switch_user: type[CliSwitchUserInterface] = CliSwitchUserInterface
    main: type[CliMainInterface] = CliMainInterface


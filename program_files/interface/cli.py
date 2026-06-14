from dataclasses import dataclass

from program_files.interface.chat.cli import CliChatInterface
from program_files.interface.session_manager.cli import CliSessionManagerInterface
from program_files.interface.edit_components.cli import CliEditComponentsInterface

@dataclass
class Cli:
    chat: type[CliChatInterface] = CliChatInterface
    session_manager: type[CliSessionManagerInterface] = CliSessionManagerInterface
    edit_components: type[CliEditComponentsInterface] = CliEditComponentsInterface


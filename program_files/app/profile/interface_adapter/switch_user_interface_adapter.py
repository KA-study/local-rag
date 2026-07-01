

from program_files.app.profile._types import SelectedUserInfo
from program_files.runtime import InterfaceMode


class SwitchUserInterfaceAdapter:

    def __init__(self):
        self._switch_user_interface = InterfaceMode.get_interface().switch_user()

    def select_user(self) -> SelectedUserInfo:
        
        self._switch_user_interface.select_user()

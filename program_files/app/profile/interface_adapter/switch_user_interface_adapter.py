from program_files.app.profile._types import NewUserIdSelected

from program_files.runtime import InterfaceMode


class SwitchUserInterfaceAdapter:

    def __init__(self):
        self._switch_user_interface = InterfaceMode.get_interface().switch_user()

    def select_user(self) -> str:

        selected_user_id: str = self._switch_user_interface.select_user()

        if selected_user_id == "_NEW_":
            raise NewUserIdSelected()

        return selected_user_id
        

    def create_user(self) -> str:
        ...


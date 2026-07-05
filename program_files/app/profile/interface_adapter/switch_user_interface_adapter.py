from program_files.app.profile._types import NewUserIdSelected

from program_files.runtime import InterfaceMode


class SwitchUserInterfaceAdapter:

    def __init__(self):
        self._switch_user_interface = InterfaceMode.get_interface().switch_user()

    def select_user(
        self,
        user_id_list: list[str]
    ) -> str:

        selected_user_id: str = self._switch_user_interface.select_user(user_id_list)

        if selected_user_id == "_NEW_":
            raise NewUserIdSelected()

        return selected_user_id


    def display(self, message: str) -> None:
        self._switch_user_interface.display(message) 
        

    def create_user(self) -> str:
        return self._switch_user_interface.create_user()



from program_files.interface.switch_user_interface.base import SwitchUserInterface


class CliSwitchUserInterface(SwitchUserInterface):

    def select_user(
        self,
        user_id_list: list[str]
    ) -> str:
        ...

    
    def display(self, message) -> None:
        print(message)

    
    def create_user(self):
        ...

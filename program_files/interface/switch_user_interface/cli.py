
from program_files.interface.switch_user_interface.base import SwitchUserInterface


class CliSwitchUserInterface(SwitchUserInterface):

    def select_user(
        self,
        user_id_list: list[str]
    ) -> str:
        self.display("user_id list:")
        for user_id in user_id_list:
            self.display(f"{user_id}")

        selected_user_id = self._input("choose user_id: ")
        return selected_user_id

    
    def display(self, message) -> None:
        print(message)

    
    def create_user(self):
        ...

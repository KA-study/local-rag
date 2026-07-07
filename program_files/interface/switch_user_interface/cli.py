
from program_files.interface.switch_user_interface.base import SwitchUserInterface


class CliSwitchUserInterface(SwitchUserInterface):

    def select_user(
        self,
        user_id_list: list[str]
    ) -> str:
        print("=== user_id list ===")

        for i, user_id in enumerate(user_id_list):
            print(f"{i}: {user_id}")

        print("n: new session")

        while True:
            choice: str = self._input("select: ")

            #new_session指定の時
            if choice == "n":
                return "_NEW_"

            #番号指定の時
            if choice.isdigit():
                idx = int(choice)

                if 0 <= idx < len(user_id_list):
                    return user_id_list[idx]

            #session_id直接指定の時
            if choice in user_id_list:

                return choice


            print("Invalid input")


    
    def display(self, message) -> None:
        print(message)

    
    def create_user(self) -> str:
        return self._input("input new user_id: ")

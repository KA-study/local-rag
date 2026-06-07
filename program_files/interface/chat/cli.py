from interface.chat.base import ChatInterface
from shared.schemas import ExitCommandError

class CliChatInterface(ChatInterface):

    def get_input(self) -> str:
        user_input = input(">>> ")

        #exit command　を確認
        self._check_exit(user_input)

        return user_input

    def display_message(self, role: str, text: str) -> None:
        print(f"{role}: {text}\n")

    def _check_exit(self, user_input: str):

        if user_input == ":q":
            raise ExitCommandError()

from program_files.interface.chat.base import ChatInterface

class CliChatInterface(ChatInterface):

    def get_input(self) -> str:
        user_input = self._input(">>> ")

        return user_input

    def display_message(self, role: str, text: str) -> None:
        print(f"{role}: {text}\n")



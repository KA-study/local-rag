from interface.chat.base import ChatInterface

class CliChatInterface(ChatInterface):

    def get_input(self) -> str:
        return input(">>> ")

    def display_message(self, role: str, text: str) -> None:
        print(f"{role}: {text}\n")

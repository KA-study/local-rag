from interface.chat.base import ChatInterface

class CliChatInterface(ChatInterface):

    def get_input(self) -> str:
        return input(">>> ")

    def output(self, text: str) -> None:
        print(text)

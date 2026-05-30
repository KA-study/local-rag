from active.ui.base import UserInterface

class CliInterface:

    def get_input(self) -> str:
        return input(">>> ")

    def output(self, text: str) -> None:
        print(text)

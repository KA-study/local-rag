

from program_files.interface.main.base import MainInterface


class CliMainInterface(MainInterface):

    def select_option(
        self,
        options: list[str]
    ) -> str:
        return self._input(f"choose option from here: {options}\n>> ")


    def display(
        self,
        message: str,
    ) -> None:
        print(message)

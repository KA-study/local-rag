from typing import Protocol

class UserInterface(Protocol):

    def get_input(self) -> str:
        ...

    def output(
        self,
        text: str
    ) -> None:
        ...

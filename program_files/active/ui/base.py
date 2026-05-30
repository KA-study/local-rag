from typing import Protocol

class UserInterface(Protocol):

    def input(self) -> str:
        ...

    def output(
        self,
        text: str
    ) -> None:
        ...

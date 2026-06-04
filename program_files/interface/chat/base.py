from typing import Protocol

class ChatInterface(Protocol):

    def get_input(self) -> str:
        ...

    def display_message(
        self,
        text: str
    ) -> None:
        ...

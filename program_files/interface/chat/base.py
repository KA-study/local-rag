from typing import Protocol

class ChatInterface(Protocol):

    def get_input(self) -> str:
        ...

    def display_message(
        self,
        role: str,
        text: str
    ) -> None:
        ...

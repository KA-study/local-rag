from abc import ABC, abstractmethod

from program_files.interface.base_interface import Interface


class ChatInterface(Interface, ABC):

    @abstractmethod
    def get_input(self) -> str:
        ...

    @abstractmethod
    def display_message(
        self,
        role: str,
        text: str
    ) -> None:
        ...


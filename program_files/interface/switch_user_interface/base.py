from abc import ABC, abstractmethod

from program_files.interface.base_interface import Interface


class SwitchUserInterface(Interface, ABC):

    @abstractmethod
    def select_user(
        self,
        user_id_list: list[str]
    ) -> str:
        ...

    @abstractmethod
    def display(self, message) -> None:
        ...

    @abstractmethod
    def create_user(self) -> str:
        ...

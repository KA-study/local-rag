from abc import ABC, abstractmethod

from program_files.interface.base_interface import Interface


class MainInterface(Interface, ABC):

    @abstractmethod
    def select_option(
        self,
        options: list[str]
    ) -> str:
        ...


    @abstractmethod
    def display(
        self,
        message: str
    ) -> None:
        ...

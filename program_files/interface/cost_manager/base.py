from abc import ABC, abstractmethod

from program_files.interface.base_interface import Interface


class CostManagerInterface(Interface, ABC):

    @abstractmethod
    def input_available_cost(self) -> float:
        ...

    @abstractmethod
    def display(self, message: str) -> None:
        ...



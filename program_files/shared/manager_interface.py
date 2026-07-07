from abc import ABC, abstractmethod


class Manager(ABC):

    @abstractmethod
    def name(self) -> str:
        ...


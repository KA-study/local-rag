from abc import ABC, abstractmethod


class Manager(ABC):

    @abstractmethod
    def name(self) -> str:
        ...


    @abstractmethod
    def run(self, app_context):
        ...

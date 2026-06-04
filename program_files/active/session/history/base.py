from abc import ABC, abstractmethod

class HistoryDB(ABC):

    @abstractmethod
    def insert_messages(self):
        ...

    @abstractmethod
    def load_messages(self):
        ...

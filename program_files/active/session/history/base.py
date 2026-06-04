from abc import ABC, abstractmethod

from active._types import Message

class HistoryDB(ABC):

    @abstractmethod
    def insert_message(self, message: Message):
        ...

    @abstractmethod
    def load_messages(self):
        ...

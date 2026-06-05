from abc import ABC, abstractmethod

from active.session._types import SessionContext

from active._types import Message

class HistoryDB(ABC):

    @abstractmethod
    def insert_message(
        self,
        message: Message,
        session_context: SessionContext
    ):
        ...

    @abstractmethod
    def load_messages(
        self,
        session_context: SessionContext
    ) -> list[Message] | None:
        ...

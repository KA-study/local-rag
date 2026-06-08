from abc import ABC, abstractmethod


from program_files.active._types import Message

class HistoryDB(ABC):

    @abstractmethod
    def insert_message(
        self,
        message: Message,
        session_id: str
    ):
        ...

    @abstractmethod
    def load_messages(
        self,
        session_id: str
    ) -> list[Message] | None:
        ...

    @abstractmethod
    def get_session_ids(
        self
    ) -> list[str]:
        ...

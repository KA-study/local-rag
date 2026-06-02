from abc import ABC, abstractmethod

from shared.schemas import Usage

class UsageDB(ABC):

    @abstractmethod
    def write_log(self, user_id: str, usage: Usage) -> None:
        ...

    @abstractmethod
    def get_status(self, user_id: str) -> dict | None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

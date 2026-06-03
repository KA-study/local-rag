from abc import ABC, abstractmethod

from shared.schemas import Usage
from infrastructure.llm.cost._types import CurrentStatus

class UsageDB(ABC):

    @abstractmethod
    def write_log(self, user_id: str, usage: Usage) -> None:
        ...

    @abstractmethod
    def get_status(self, user_id: str) -> CurrentStatus | None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

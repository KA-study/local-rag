from abc import ABC, abstractmethod

from shared.schemas import Usage
from infrastructure.llm.cost._types import CurrentStatus

class UsageDB(ABC):

    @abstractmethod
    def write_log_and_status(self, usage: Usage) -> None:
        ...

    @abstractmethod
    def get_status(self) -> CurrentStatus | None:
        ...

    @abstractmethod
    def close(self) -> None:
        ...

    @abstractmethod
    def set_available_cost(self, available_cost: float) -> None:
        ...

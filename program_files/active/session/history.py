from dataclasses import dataclass
from typing import Literal

Role = Literal["user", "assistant"]

@dataclass(slots=True)
class Message:
    role: Role
    content: str


class History:

    def __init__(self) -> None:
        self._messages: list[Message] = []

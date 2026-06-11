from dataclasses import dataclass
from typing import Literal

@dataclass
class SessionContext:
    session_id: str

Role = Literal["user", "assistant"]

@dataclass(slots=True)
class Message:
    role: Role
    content: str




from typing import Literal
from dataclasses import dataclass


Role = Literal["user", "assistant"]

@dataclass(slots=True)
class Message:
    role: Role
    content: str




from typing import Literal, TypedDict

class HistoryEntry(TypedDict):
    role: Literal["user", "llm"]
    content: str

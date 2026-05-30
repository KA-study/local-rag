from dataclasses import dataclass 

from interface._types import HistoryEntry


@dataclass
class Session:
    session_id: str
    history: list[HistoryEntry] 

    def add_user_message(self, message: str) -> None:
        history_entry: HistoryEntry = {
            "role": "user",
            "content": message
        }

        self.history.append(history_entry)

    def add_llm_message(self, message: str) -> None:
        history_entry: HistoryEntry = {
            "role": "llm",
            "content": message
        }

        self.history.append(history_entry)

    def get_history(self) -> list[HistoryEntry]:
        return self.history

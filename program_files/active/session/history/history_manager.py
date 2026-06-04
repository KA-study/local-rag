

from active.session.history.base import HistoryDB
from active.session._types import SessionContext
from active._types import Message
from app.context import AppContext


class HistoryManager:

    def __init__(
        self,
        app_context: AppContext,
        session_context: SessionContext,
        history_db: HistoryDB
    ):
        self._history_db = history_db

    def save_history(self, message: Message):
        self._history_db.insert_message(message)

    def load_history(self) -> list[Message] | None:
        return self._history_db.load_messages()




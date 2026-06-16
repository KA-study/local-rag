

from program_files.session.history.base import HistoryDB
from program_files.session.history.history_db import SQliteHistoryDB
from program_files.session._types import SessionContext
from program_files.session._types import Message
from program_files.app.context.context import AppContext


class HistoryManager:

    def __init__(
        self,
        app_context: AppContext,
    ):
        self._history_db: HistoryDB = SQliteHistoryDB(
            app_context,
            db_path="~/projects/local_rag/data/history.db"
        )

    def save_history(
        self,
        message: Message,
        session_context: SessionContext
    ):
        self._history_db.insert_message(
            message,
            session_context.session_id
        )

    def load_history(
        self,
        session_context: SessionContext
    ) -> list[Message] | None:

        return self._history_db.load_messages(
            session_context.session_id
        )

    def get_session_contexts(self) -> list[SessionContext]:

        session_ids: list[str] = self._history_db.get_session_ids()
            
        session_contexts: list[SessionContext] = [
            SessionContext(session_id=session_id)
            for session_id in session_ids
                ]

        return session_contexts





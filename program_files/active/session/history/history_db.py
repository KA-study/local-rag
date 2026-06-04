import sqlite3

from active.session.history._types import CREATE_HISTORY_DB
from active.session.history.base import HistoryDB
from active.session._types import SessionContext
from active._types import Message
from app.context import AppContext


def SQliteHistoryDB(HistoryDB):

    def __init__(
        self,
        app_context: AppContext,
        session_context: SessionContext,
        db_path: str = "history.db"
    ):
        self._conn = sqlite3.connect(self.db_path)
        self._app_context = app_context
        self._session_context = session_context

        self._init_table()


    def _init_table(self) -> None:
        self._conn.execute(CREATE_HISTORY_DB)
        

    def insert_messages(self, message: Message) -> None:
       
        user_id = self._app_context.user_id
        session_id = self._session_context.session_id

        self._conn.execute(
            """
                INSERT INTO messages (user_id, session_id, role, content)
                VALUES (?, ?, ?, ?)
            """, 
            (
                user_id,
                session_id,
                message.role,
                message.content
            )
        )




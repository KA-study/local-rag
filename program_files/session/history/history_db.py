import sqlite3

from program_files.session.history._types import CREATE_HISTORY_DB
from program_files.session.history.base import HistoryDB
from program_files.session._types import Message
from program_files.app.context.context import AppContext
from program_files.app.registry.components_registry import ComponentsRegistry
from program_files.shared.config import DEFAULT_HISOTRY_DB_PATH


@ComponentsRegistry.component(
    base=HistoryDB,
    name="sqlite_history_db"
)
class SQliteHistoryDB(HistoryDB):

    def __init__(
        self,
        app_context: AppContext,
        db_path = DEFAULT_HISOTRY_DB_PATH
    ):
        self._conn = sqlite3.connect(db_path)
        self._init_table()
        self._app_context = app_context


    def _init_table(self) -> None:
        self._conn.execute(CREATE_HISTORY_DB)
        

    def insert_message(
        self,
        message: Message,
        session_id: str
    ) -> None:
       
        user_id = self._app_context.user_id

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


    def load_messages(
        self,
        session_id: str
    ) -> list[Message] | None:

        user_id = self._app_context.user_id

        rows = self._conn.execute(
            """
                SELECT role, content
                FROM messages
                WHERE user_id = ?
                AND session_id = ?
                ORDER BY message_id ASC
            """,
            (
                user_id,
                session_id
            )
        ).fetchall()

        role_index = 0
        content_index = 1
        created_at_index = 2

        messages = [
            Message(
                role=r[role_index],
                content=r[content_index]
            )
            for r in rows
        ]

        return messages

    
    def get_session_ids(self) -> list[str]:

        user_id = self._app_context.user_id

        rows = self._conn.execute(
            """
                SELECT session_id
                FROM messages
                WHERE user_id = ?
                ORDER BY message_id ASC
            """,
            (
                user_id,
            )
        ).fetchall()

        session_id = 0

        session_id = [
            r[session_id]
            for r in rows
        ]

        return session_id



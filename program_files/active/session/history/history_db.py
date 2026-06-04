import sqlite3

from active.session.history._types import CREATE_HISTORY_DB
from active.session.history.base import HistoryDB


def SQliteHistoryDB(HistoryDB):

    def __init__(self, db_path: str = "history.db"):
        self._conn = sqlite3.connect(self.db_path)

        self._init_table()


    def _init_table(self) -> None:
        self._conn.execute(CREATE_HISTORY_DB)
        


import sqlite3

from infrastructure.llm.cost.base import UsageDB
from infrastructure.llm.cost.service import calc_cost
from infrastructure.llm.cost._types import (
    CREATE_CURRENT_STATUS_TABLE,
    CREATE_USAGE_LOG_TABLE
)
from shared.schemas import Usage


class SQliteUsageDB(UsageDB):

    def __init__(self, db_path: str = "usage.db"):
        self._conn = sqlite3.connect(db_path)
        self._conn.row_factory = sqlite3.Row  # dict風アクセス用

        self._init_tables()


    def _init_tables(self) -> None:

        self._conn.execute(CREATE_USAGE_LOG_TABLE)
        self._conn.execute(CREATE_CURRENT_STATUS_TABLE)


    def write_log(self, user_id: str, usage: Usage) -> None:
        
        cost = calc_cost(usage.input_tokens, usage.output_tokens, usage.model_name)

        try:
            #トランザクション開始
            #sqlite3は自動でトランザクションするから、以下はコメントアウト
            #self._conn.execute("BEGIN")

            #usage_logへ記録
            self._conn.execute(
                """
                INSERT INTO usage_log (
                    user_id,
                    model_name,
                    input_tokens,
                    output_tokens,
                    cost
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    usage.model_name,
                    usage.input_tokens,
                    usage.output_tokens,
                    cost
                )
            )

            #current_status更新
            self._conn.execute(
                """
                INSERT INTO current_status (
                    user_id,
                    total_input_tokens,
                    total_output_tokens,
                    total_cost
                )
                VALUES (?, ?, ?, ?)
                ON CONFLICT(user_id)
                DO UPDATE SET
                    total_input_tokens =
                        total_input_tokens + excluded.total_input_tokens,
                    total_output_tokens =
                        total_output_tokens + excluded.total_output_tokens,
                    total_cost =
                        total_cost + excluded.total_cost               
                """,
                (
                    user_id,
                    usage.input_tokens,
                    usage.output_tokens,
                    cost
                ),
            )

            self._conn.commit()

        except sqlite3.Error:

            self._conn.rollback()
            raise 


    def get_status(self, user_id: str) -> dict | None:
        row = self._conn.execute(
            """
            SELECT * FROM current_status
            WHERE user_id = ?
            """,
            (user_id,)
        ).fetchone()

        if row is None:
            return None

        return dict(row)


    def close(self) -> None:
        self._conn.close()


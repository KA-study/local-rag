

from infrastructure.llm.cost.usage_db import SQliteUsageDB
from infrastructure.llm.cost._types import CurrentStatus
from shared.schemas import Usage


class CostManager:

    #ここではSqliteUsageDBなど固定だが、最終的には上から引数としてもらう形にする。
    def __init__(self):
        self._usage_db = SQliteUsageDB()

    def check_allowance(self):
        ...

    def write_log(self, user_id: str, usage_db: Usage):
        self._usage_db.write_log(user_id, usage_db)

    def get_status(self, user_id: str) -> CurrentStatus | None:
        return self._usage_db.get_status(user_id)

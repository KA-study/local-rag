from infrastructure.llm.cost.base import UsageDB

from shared.schemas import Usage


class SQliteUsageDB(UsageDB):

    def __init__(self, db_path: str = "usage.db"):
        ...
    

    def write_log(self, user_id: str, usage: Usage) -> None:
        ...

    def get_status(self, user_id: str) -> dict | None:
        ...

    def close(self) -> None:
        ...



from program_files.infrastructure.llm.cost.usage_db import SQliteUsageDB
from program_files.infrastructure.llm.cost._types import CurrentStatus
from program_files.infrastructure.llm.interface_adapter.cost_manager import CostManagerInterfaceAdapter
from program_files.shared.schemas import Usage
from program_files.app.context.context import AppContext


class CostManager:

    #ここではSqliteUsageDBなど固定だが、最終的には上から引数としてもらう形にする。
    def __init__(self, app_context: AppContext):
        self._usage_db = SQliteUsageDB(app_context)
        self._user_id = app_context.user_id
        self._interface = CostManagerInterfaceAdapter()

    def check_allowance(self):
        current_status: CurrentStatus | None = self._usage_db.get_status()

        if current_status is None:
            raise ValueError(f"Unregistored user: {self._user_id}. set available_cost.")

        if current_status["total_cost"] >= current_status["available_cost"]:
            raise ValueError("cost over.")


    def write_log_and_status(self, usage_db: Usage):
        self._usage_db.write_log_and_status(usage_db)

    def get_status(self) -> CurrentStatus | None:
        return self._usage_db.get_status()

    def set_available_cost(self) -> None:
        new_available_cost: float =  self._interface.input_available_cost()

        self._usage_db.set_available_cost(new_available_cost)
       

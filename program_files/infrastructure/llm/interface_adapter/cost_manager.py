
from program_files.interface.cli import Cli


class CostManagerInterfaceAdapter:

    def __init__(self):
        self._interface = Cli.cost_manager()

    def input_available_cost(self) -> float:
        return self._interface.input_available_cost()

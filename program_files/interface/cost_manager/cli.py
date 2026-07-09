
from program_files.interface.cost_manager.base import CostManagerInterface



class CliCostManagerInterface(CostManagerInterface):

    def input_available_cost(self) -> float:
        while True:
            user_input = self._input("new available cost (with float)\n>> ")

            try:
                value = float(user_input)
                break

            except ValueError:
                print(f"{user_input} is not float.")

        return value


    def display(self, message: str) -> None:
        print(message)

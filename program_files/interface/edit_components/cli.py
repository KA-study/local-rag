from program_files.interface.edit_components.base import EditComponentsInterface
from program_files.shared.schemas import ComponentsTreeNode

class CliEditComponentsInterface(EditComponentsInterface):

    def get_input(self) -> str:
        return input("> ")

    def display_list(
        self,
        components_tree: ComponentsTreeNode,
    ) -> None:
        ...

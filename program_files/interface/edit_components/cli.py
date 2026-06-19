from program_files.interface.edit_components.base import EditComponentsInterface
from program_files.shared.schemas import ComponentsTreeNode

class CliEditComponentsInterface(EditComponentsInterface):

    def get_input(self) -> str:
        return input("> ")


    def display_list(
        self,
        components_tree: ComponentsTreeNode,
    ) -> None:
        self._display_node(components_tree)


    def _display_node(
        self,
        node: ComponentsTreeNode,
        depth: int = 0,
    ) -> None:
        indent = "    " * depth

        # 葉ノード
        if node.current is not None and not node.children:
            print(f"{indent}{node.name} ... {node.current}")
            return

        # 枝ノード
        print(f"{indent}{node.name}")

        for child in node.children:
            self._display_node(child, depth + 1)

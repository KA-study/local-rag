from program_files.interface.edit_components.base import EditComponentsInterface
from program_files.shared.schemas import (
    ComponentsTreeNode,
    EditRequest,
)

class CliEditComponentsInterface(EditComponentsInterface):
    
    def select_change(
        self,
        components_tree: ComponentsTreeNode
    ) -> EditRequest:

        #display the list of components
        self._display_node(components_tree) 

        #get_input
        while True:
            try:
                edit_request = self._get_input(components_tree)
                break
            except ValueError:
                print(f"no components was found. try again.")

        return edit_request

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

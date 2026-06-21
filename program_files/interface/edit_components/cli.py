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


    def _get_input(
        self,
        components_tree: ComponentsTreeNode
    ) -> EditRequest:
        user_input: str = self._input("> ")

        """
        - user_inputの形式
        path name
        - 具体例
        session.history_db sqlite_history_db
        """

        path_str: str
        name: str

        path_str, name = user_input.split(" ")

        path: list[str] = path_str.split(".")

        #build EditRequest
        if self._verify_with_node(
            path=path,
            selected_name=name,
            node=components_tree,
            ):

            request = EditRequest(
                path=tuple(path),
                selected_name=name
            )

            return request
        
        raise ValueError()


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


    def _verify_with_node(
        self,
        path: list[str],
        selected_name: str,
        node: ComponentsTreeNode,
        depth: int = 0
    ) -> bool:

        # at a terminal point
        if depth == len(path):
            return (
                node.choices is not None
                and selected_name in node.choices
            )

        target_name = path[depth]

        #ComponentsTreeNodeの一番上の親がComponentsなのに対して、
        #user_inputからのpathは、その下、SessionComponents等からであるから。
        for child in node.children:
            if child.name == target_name:
                return self._verify_with_node(
                    path,
                    selected_name,
                    child,
                    depth + 1,
                )

        return False










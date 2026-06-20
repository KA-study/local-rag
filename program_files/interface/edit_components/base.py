from typing import Protocol
from program_files.shared.schemas import (
    ComponentsTreeNode,
    EditRequest,
)


class EditComponentsInterface(Protocol):

    def select_change(
        self,
        components_tree: ComponentsTreeNode
        ) -> EditRequest:
        ...

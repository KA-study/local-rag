from abc import ABC, abstractmethod
from program_files.shared.schemas import (
    ComponentsTreeNode,
    EditRequest,
)

from program_files.interface.base.base_interface import Interface


class EditComponentsInterface(Interface, ABC):

    @abstractmethod
    def select_change(
        self,
        components_tree: ComponentsTreeNode
        ) -> EditRequest:
        ...

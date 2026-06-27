from abc import ABC, abstractmethod
from program_files.shared.schemas import (
    TreeNode,
    EditRequest,
)

from program_files.interface.base_interface import Interface


class EditTreeInterface(Interface, ABC):

    @abstractmethod
    def select_change(
        self,
        tree: TreeNode
        ) -> EditRequest:
        ...

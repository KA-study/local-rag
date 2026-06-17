from typing import Protocol
from program_files.shared.schemas import ComponentsTreeNode


class EditComponentsInterface(Protocol):

    #ここは単純に、入力を受け取るだけ。それ以上の処理はAdapterで行う。
    def get_input(self) -> str:
        ...

    #現在選択されているComponentsと、選択可能なComponentsの表示
    def display_list(
        self,
        components_tree: ComponentsTreeNode,
    ):
        ...

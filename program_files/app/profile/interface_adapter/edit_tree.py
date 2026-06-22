from dataclasses import is_dataclass, fields

from program_files.runtime import Runtime
from program_files.shared.schemas import (
    TreeNode,
    EditRequest,
)
from program_files.app.context.components import Components
from program_files.app.registry.components_registry import ComponentsRegistry
from program_files.interface.edit_tree.base import EditTreeInterface

class EditTreeInterfaceAdapter:
    
    def __init__(self):
        self._edit_components_interface: EditTreeInterface = Runtime.get_interface().edit_components()

    def select_change(
        self,
        obj
    ) -> EditRequest:
        
        #build components_tree
        tree: TreeNode = self._build_tree(
            name="components",
            obj=obj
        )

        #return EditRequest.
        request: EditRequest = self._edit_components_interface.select_change(tree)
        
        return request


    #再帰処理
    def _build_tree(
        self,
        name: str,
        obj: object
    ) -> TreeNode:

        #枝部分処理
        if is_dataclass(obj):
            return TreeNode(
                name=name,
                current=None,
                choices=None,
                children=[
                    self._build_tree(field.name, getattr(obj, field.name))
                    for field in fields(obj)
                ]
            )

        #葉部分処理
        return TreeNode(
            name=name,
            current=ComponentsRegistry.get_name(type[obj]),       #仮置き
            choices=[
                choice.name
                for choice in ComponentsRegistry.get_choices_for_implementation(type[obj])
            ],#仮置き
            children=[]
        )


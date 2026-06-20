from dataclasses import is_dataclass, fields

from program_files.runtime import Runtime
from program_files.shared.schemas import (
    ComponentsTreeNode,
    EditRequest,
)
from program_files.app.context.components import Components
from program_files.app.registry.components_registry import ComponentsRegistry
from program_files.interface.edit_components.base import EditComponentsInterface

class EditComponentsInterfaceAdapter:
    
    def __init__(self):
        self._edit_components_interface: EditComponentsInterface = Runtime.get_interface().edit_components()

    def select_change(
        self,
        components: Components
    ) -> EditRequest:
        
        #build components_tree
        components_tree: ComponentsTreeNode = self._build_tree(
            name="components",
            obj=components
        )

        #return EditRequest.
        request: EditRequest = self._edit_components_interface.select_change(components_tree)
        
        return request


    #再帰処理
    def _build_tree(
        self,
        name: str,
        obj: object
    ) -> ComponentsTreeNode:

        #枝部分処理
        if is_dataclass(obj):
            return ComponentsTreeNode(
                name=name,
                current=None,
                choices=None,
                children=[
                    self._build_tree(field.name, getattr(obj, field.name))
                    for field in fields(obj)
                ]
            )

        #葉部分処理
        return ComponentsTreeNode(
            name=name,
            current=ComponentsRegistry.get_name(type[obj]),       #仮置き
            choices=[
                choice.name
                for choice in ComponentsRegistry.get_choices_for_implementation(type[obj])
            ],#仮置き
            children=[]
        )


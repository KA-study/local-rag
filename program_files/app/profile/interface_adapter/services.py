from dataclasses import fields, is_dataclass

from program_files.shared.schemas import ComponentsTreeNode
from program_files.app.registry.components_registry import ComponentsRegistry


#再帰処理
def build_tree(name: str, obj: object) -> ComponentsTreeNode:
    #枝部分処理
    if is_dataclass(obj):
        return ComponentsTreeNode(
            name=name,
            current=None,
            choices=None,
            children=[
                build_tree(field.name, getattr(obj, field.name))
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

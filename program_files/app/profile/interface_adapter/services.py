from dataclasses import fields, is_dataclass

from program_files.shared.schemas import ComponentsTreeNode


def build_tree(name: str, obj: object) -> ComponentTreeNode:
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
        current=obj.__name__,       #仮置き
        choices=get_choices(obj),   #仮置き
        children=[]
    )

from program_files.runtime import Runtime
from program_files.shared.schemas import ComponentsTreeNode
from program_files.app.context.components import Components
from program_files.interface.edit_components.base import EditComponentsInterface
from program_files.app.profile.interface_adapter.services import build_tree

class EditComponentsInterfaceAdapter:
    
    def __init__(self):
        self._edit_components_interface: EditComponentsInterface = Runtime.get_interface().edit_components()


    def get_input(self):
        return self._edit_components_interface.get_input()

    def display_list(
        self,
        components: Components
    ) -> None:

        components_tree: ComponentsTreeNode = build_tree(
            name="components",
            obj=components
        )

        self._edit_components_interface.display_list(components_tree)
      

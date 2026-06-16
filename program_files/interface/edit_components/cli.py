from dataclasses import field

from program_files.interface.edit_components.base import EditComponentsInterface
from program_files.app.context.components import Components

class CliEditComponentsInterface(EditComponentsInterface):

    def get_input(self) -> str:
        return input("> ")

    def display_list(
        self,
        components: Components,
    ) -> None:

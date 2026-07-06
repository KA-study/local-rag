

from program_files.interface.cli import Cli
from program_files.interface.gui import Gui


class InterfaceMode:

    _interface: Cli | Gui | None = None


    @classmethod
    def set_cli(
        cls,
    ):
        if cls._interface :
            raise ValueError("An interface has been already setted.")

        cls._interface = Cli()

    @classmethod
    def set_gui(
        cls,
    ):
        if cls._interface :
            raise ValueError("An interface has been already setted.")

        cls._interface = Gui()

    @classmethod
    def get_interface(
        cls,
    ) -> Cli | Gui:
        return cls._interface

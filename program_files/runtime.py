

from program_files.interface.cli import Cli
from program_files.interface.gui import Gui


class InterfaceMode:
    _interface: Cli | Gui

    @classmethod
    def set_interface_type(cls) -> None:

        while True:
            user_input = input("choose interface: Cli or Gui\n>> ")
        
            if user_input == "Cli" or "cli":
                cls._set_cli()
                break
            elif user_input == "Gui" or "gui":
                cls._set_gui()
                break
            else:
                print(f"Invalid InterfaceMode: {user_input}")


    @classmethod
    def _set_cli(
        cls,
    ):
        if cls._interface :
            raise ValueError("An interface has been already setted.")

        cls._interface = Cli()

    @classmethod
    def _set_gui(
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

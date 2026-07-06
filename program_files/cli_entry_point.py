

from program_files.main import Main
from program_files.runtime import InterfaceMode

def cli_entry_point():
    
    InterfaceMode.set_cli()

    Main().run()


cli_entry_point()

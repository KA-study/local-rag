

from program_files.main import main
from program_files.runtime import InterfaceMode

def cli_entry_point():
    
    InterfaceMode.set_cli()

    main()


cli_entry_point()



from program_files.main import main
from program_files.runtime import Runtime

def cli_entry_point():
    
    Runtime.set_cli()

    main()


cli_entry_point()



from program_files.main import main
from program_files.runtime import Runtime

def gui_entry_point():

    Runtime.set_gui()

    main()


gui_entry_point()

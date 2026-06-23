

from program_files.main import main
from program_files.runtime import InterfaceMode

def gui_entry_point():

    InterfaceMode.set_gui()

    main()


gui_entry_point()

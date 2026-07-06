

from program_files.main import Main
from program_files.runtime import InterfaceMode

def gui_entry_point():

    InterfaceMode.set_gui()

    Main().run()


gui_entry_point()



from program_files.app.context.context import AppContext
from program_files.session.manager import SessionManager
from program_files.passive.passive_operator import PassiveManager
from program_files.app.profile.profile_run import ProfileManager
from program_files.runtime import InterfaceMode

class MainInterfaceAdapter:

    def __init__(
        self,
        app_context: AppContext
    ):
        self._managers = {
            "session": SessionManager(app_context),
            "passive": PassiveManager(),
            "profile": ProfileManager(),
        }
        self._interface = InterfaceMode.get_interface().main()
    
    def select_option(self):
        
        while True:
            options: list[str] = [manager.name() for manager in self._managers.values()]

            user_input = self._interface.select_option(options)

            if user_input in options:
                return user_input

            self._interface.display(f"Invalid option: {user_input}")

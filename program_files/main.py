

from program_files.app.context.context import AppContext
from program_files.app.profile.profile_service import ProfileService
from program_files.main_interface_adapter import MainInterfaceAdapter
from program_files.shared.schemas import ExitCommandError
from program_files.shared.config import PROJECT_ROOT


from program_files.app.profile.profile_run import ProfileManager
from program_files.passive.passive_operator import PassiveManager
from program_files.session.manager import SessionManager


"""
- SessionManager entry point
- Profile entry point
- PassiveOperator entry point
"""

class Main:

    def __init__(self):
        self._app_context: AppContext


    def run(self):
        print(PROJECT_ROOT)
        print(PROJECT_ROOT.exists())

        profile_service = ProfileService()
        
        #前回のuser_id呼び出し。ない場合は新規作成
        try:
            self._app_context: AppContext = profile_service.load_latest_app_context()
        except FileNotFoundError or KeyError as ex:
            print(f"Error: {ex}")
            self._app_context: AppContext = profile_service.create_user_for_main()

        interface = MainInterfaceAdapter(self._app_context)

        try:
            option_class_instance = interface.select_option()

            match(option_class_instance):
                case ProfileManager():
                    self._app_context = option_class_instance.run(self._app_context)

                case PassiveManager():
                    option_class_instance.run()

                case SessionManager():
                    option_class_instance.run()

                case _:
                    raise ValueError("for developer: unregistered Manager was selected.")
                


        except ExitCommandError:
            print("sccessfully finished.")


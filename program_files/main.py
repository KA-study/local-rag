

from program_files.app.context.context import AppContext
from program_files.app.profile.profile_service import ProfileService
from program_files.main_interface_adapter import MainInterfaceAdapter
from program_files.app.profile.app_context_generator.app_context_generator import AppContextGenerator
from program_files.shared.schemas import ExitCommandError
from program_files.shared.config import PROJECT_ROOT


"""
- SessionManager entry point
- Profile entry point
- PassiveOperator entry point
"""

class Main:

    def run(self):
        print(PROJECT_ROOT)
        print(PROJECT_ROOT.exists())

        profile_service = ProfileService()
        
        #前回のuser_id呼び出し。ない場合は新規作成
        try:
            app_context: AppContext = profile_service.load_latest_app_context()
        except FileNotFoundError or KeyError:
            app_context: AppContext = profile_service.create_user()

        interface = MainInterfaceAdapter(app_context)

        try:
            option_class_instance = interface.select_option()
            option_class_instance.run(app_context)

        except ExitCommandError:
            print("sccessfully finished.")


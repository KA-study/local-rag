

from program_files.app.context.context import AppContext
from program_files.app.profile.profile_service import ProfileService
from program_files.main_interface_adapter import MainInterfaceAdapter
from program_files.app.profile.interface_adapter.switch_user_interface_adapter import SwitchUserInterfaceAdapter
from program_files.app.profile.app_context_generator.app_context_generator import AppContextGenerator


"""
- SessionManager entry point
- Profile entry point
- PassiveOperator entry point
"""

class Main:

    def run(self):
        profile_service = ProfileService()
        
        try:
            app_context: AppContext = profile_service.load_latest_app_context()
        except FileNotFoundError or KeyError:
            user_id: str = SwitchUserInterfaceAdapter().create_user()
            app_context: AppContext = AppContextGenerator().generate_app_context(
                user_id=user_id
            )

        
        interface = MainInterfaceAdapter(app_context)

        interface.select_option()


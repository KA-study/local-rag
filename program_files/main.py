

from program_files.app.context.context import AppContext
from program_files.app.profile.profile_service import ProfileService
from program_files.main_interface_adapter import MainInterfaceAdapter

"""
- SessionManager entry point
- Profile entry point
- PassiveOperator entry point
"""

def main():

    profile_service = ProfileService()

    app_context: AppContext = profile_service.load_latest_app_context()
    
    interface = MainInterfaceAdapter(app_context)

    interface.select_option()


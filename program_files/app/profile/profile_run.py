

from program_files.app.context.context import AppContext
from program_files.app.profile.profile_service import ProfileService
from program_files.app.profile.interface_adapter.profile_run import ProfileRunInterfaceAdapter
from program_files.shared.schemas import ExitCommandError


class ProfileManager:

    def __init__(
        self,
    ):
        self._profile_service = ProfileService()
        self._profile_run_interface = ProfileRunInterfaceAdapter()

    def name(self):
        return "profile_settings"


    def run(
        self,
        app_context: AppContext
    ) -> AppContext:
        
        while True:
            """
            choose an option: switch_user, edit_components or edit_user_config.
            """
            ProfileOptionMap = {
                "switch_user": self._profile_service.switch_user,
                "edit_components": self._components_run,
                "edit_user_config": self._user_config_run,
            }

            try:
                user_select: str = self._profile_run_interface.select_option(ProfileOptionMap)
            except ExitCommandError:
                break

            #ProfileOptionMapに含まれるすべての関数の引数は、AppContextのみに統一
            app_context = ProfileOptionMap[user_select](app_context)

        return app_context


    def _components_run(
        self,
        app_context: AppContext
    ) -> AppContext:

        #AppContext is frozen.
        while True:
            try:
                app_context = self._profile_service.edit_components(app_context)
            except ExitCommandError:
                break

        return app_context


    def _user_config_run(
        self,
        app_context: AppContext
    ) -> AppContext:
        
        while True:
            try:
                app_context = self._profile_service.edit_user_config(app_context)
            except ExitCommandError:
                break

        return app_context

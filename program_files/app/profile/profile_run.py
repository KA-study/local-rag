

from program_files.app.context.context import AppContext
from program_files.app.profile.profile_service import ProfileService
from program_files.shared.schemas import ExitCommandError



class ProfileRun:

    def __init__(
        self,
    ):
        self._profile_service = ProfileService()

    def run(
        self,
        app_context: AppContext
    ) -> AppContext:
        ...

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

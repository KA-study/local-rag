

from program_files.app.context.context import AppContext
from program_files.app.profile.app_context_generator._types import (
    DEFAULT_USER_ID,
    DEFAULT_COMPONENTS,
    DEFAULT_USER_CONFIG,
)


class AppContextGenerator:

    def generate_app_context(
        self,
        user_id=DEFAULT_USER_ID,
        components=DEFAULT_COMPONENTS,
        user_config=DEFAULT_USER_CONFIG
    ) -> AppContext:
        return AppContext(
            user_id = user_id,
            components = components,
            user_config = user_config
        )



from program_files.app.context.context import AppContext


class ProfileJsonManager:

    def load(
        self,
        user_id: str
    ) -> AppContext:
        ...

    def save(
        self,
        app_context: AppContext
    ) -> None:
        ...

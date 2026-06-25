

from program_files.app.context.context import AppContext
from program_files.app.context.components import Components


class ProfileStorageManager:

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

    def _app_context_to_json(
        self,
        app_context: AppContext
    ) -> dict:
        ...

    def _json_to_app_context(
        self,
        json: dict
    ) -> AppContext:
        ...

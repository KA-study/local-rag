

from program_files.app.context.context import AppContext
from program_files.app.context.components import Components

class AppState:
    
    def __init__(self):
        self._context = AppContext() #frozen

    #保存データへのアクセスあり
    def load_latest_app_context(self):
        ...

    #保存データへのアクセスあり
    def switch_user(self):
        ...

    def edit_components(
        self,
        app_context: AppContext
    ) -> AppContext:
        components: Components = app_context.components

    def edit_user_config(self):
        ...

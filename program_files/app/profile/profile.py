

from program_files.app.context.context import AppContext
from program_files.app.context.components import Components
from program_files.app.profile.interface_adapter.edit_components import EditComponentsInterfaceAdapter
from program_files.shared.schemas import EditRequest

class ProfileManager:
    
    def __init__(self):
        self._context = AppContext() #frozen
        self._interface_adapter = EditComponentsInterfaceAdapter()

    #保存データへのアクセスあり
    def load_latest_app_context(self):
        ...

    #セッティングのセーブ
    def save_components_and_config(self):
        ...

    #保存データへのアクセスあり
    def switch_user(self):
        ...

    def edit_components(
        self,
        app_context: AppContext
    ) -> AppContext:
        components: Components = app_context.components

        #select component.
        request: EditRequest = self._interface_adapter.select_change(components)

        #save changed components automatically.
        

    def edit_user_config(self):
        ...

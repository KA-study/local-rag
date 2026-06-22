from program_files.app.context.context import AppContext
from program_files.app.context.components import Components
from program_files.app.context.user_config import UserConfig
from program_files.app.profile.interface_adapter.edit_tree import EditTreeInterfaceAdapter
from program_files.shared.schemas import EditRequest

class ProfileManager:
    
    def __init__(self):
        self._context = AppContext() #frozen
        self._interface_adapter = EditTreeInterfaceAdapter()

    #保存データへのアクセスあり
    def _load_latest_app_context(self):
        ...

    #セッティングのセーブ
    def _save_components_and_config(self):
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
        #先にedit_user_configをcomponentsと同じように作り、その後save_componentsなどを作り、最後に完成させる。
        

    def edit_user_config(
        self,
        app_context: AppContext
    ) -> AppContext:
        user_config: UserConfig = app_context.user_config

        #select user_config
        request: EditRequest = self._interface_adapter.select_change(user_config)



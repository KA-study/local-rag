from program_files.app.context.context import AppContext
from program_files.app.context.components import Components
from program_files.app.context.user_config import UserConfig
from program_files.app.profile.interface_adapter.edit_tree import EditTreeInterfaceAdapter
from program_files.app.profile.profile_json_storage.profile_storage_manager import ProfileStorageManager
from program_files.shared.schemas import EditRequest

class ProfileService:
    
    def __init__(
        self,
    ):
        self._interface_adapter = EditTreeInterfaceAdapter()
        self._profile_storage_manager = ProfileStorageManager()


    #保存データへのアクセスあり
    def _load_latest_app_context(
        self,
    ) -> AppContext:
        ...

    #セッティングのセーブ
    def _save_components_and_config(
        self,
        app_context: AppContext
    ):
        self._profile_storage_manager.save(app_context)


    #保存データへのアクセスあり
    def switch_user(
        self,
        app_context: AppContext
    ) -> AppContext:
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



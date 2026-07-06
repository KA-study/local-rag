from dataclasses import replace, fields
from typing import cast

from program_files.app.context.context import AppContext
from program_files.app.context.components import Components
from program_files.app.context.user_config import UserConfig
from program_files.app.registry.components_registry import ComponentsRegistry
from program_files.app.profile.interface_adapter.edit_tree import EditTreeInterfaceAdapter
from program_files.app.profile.interface_adapter.switch_user_interface_adapter import SwitchUserInterfaceAdapter
from program_files.app.profile.profile_json_storage.profile_storage_manager import ProfileStorageManager
from program_files.app.profile._types import NewUserIdSelected
from program_files.app.profile.profile_json_storage.latest_user_id_store_manager import LatestUserIdStoreManager
from program_files.app.profile.app_context_generator.app_context_generator import AppContextGenerator
from program_files.shared.schemas import EditRequest

class ProfileService:
    
    def __init__(
        self,
    ):
        self._interface_adapter = EditTreeInterfaceAdapter()
        self._switch_user_interface_adapter = SwitchUserInterfaceAdapter()
        self._profile_storage_manager = ProfileStorageManager()
        self._latest_user_id_store_manager = LatestUserIdStoreManager()


    #保存データへのアクセスあり
    def load_latest_app_context(
        self,
    ) -> AppContext:

        latest_user_id: str = self._latest_user_id_store_manager.load()

        latest_app_context: AppContext = self._profile_storage_manager.load(latest_user_id)

        return latest_app_context


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
        app_context_list: list[AppContext] = self._profile_storage_manager.get_all_app_context()
        user_id_list: list[str] = [app_context.user_id for app_context in app_context_list]

       
        try:
            #既存のuser_idに含まれているかのチェック、処理
            while True:
                selected_user_id: str = self._switch_user_interface_adapter.select_user(user_id_list)

                selected_app_context = None

                for app_context in app_context_list:
                    if app_context.user_id == selected_user_id:
                        selected_app_context = app_context
                        break

                if selected_app_context is None:
                    self._switch_user_interface_adapter.display(
                        f"Unregisterd user_id: {selected_user_id}"
                    )
                    continue

                break
                
        except NewUserIdSelected:
            while True:
                new_user_id: str = self._switch_user_interface_adapter.create_user()

                if new_user_id in user_id_list:
                    continue

                selected_app_context = AppContextGenerator().generate_app_context(user_id=new_user_id)

                #ProfileStorageへの登録
                self._profile_storage_manager.save(selected_app_context)

        return selected_app_context



    def edit_components(
        self,
        app_context: AppContext,
    ) -> AppContext:

        components = app_context.components

        # select component
        request_for_components = self._interface_adapter.select_change(components)

        # pathをたどり、最後のフィールドを持つオブジェクトまで移動
        obj = components

        #[:-1]は、後ろから数えて一番目の一つ前、つまり後ろから数えて二番目までをforで回す
        for field_name in request_for_components.path[:-1]:
            obj = getattr(obj, field_name)

        target_field_name = request_for_components.path[-1]

        # 最後のフィールドの型(base)を取得
        for field in fields(obj):
            if field.name == target_field_name:
                base = field.type
                break
        else:
            raise ValueError(f"{target_field_name} does not exist.")

        selected_type = ComponentsRegistry.get_type(
            cast(
                type,
                base
            ),
            request_for_components.selected_name,
        )

        new_components = cast(
            Components,
            self._replace_path_following_to_edit_request(
                obj=components,
                path=request_for_components.path,
                value=selected_type,
            ),
        )

        new_app_context = AppContext(
            user_id=app_context.user_id,
            components=new_components,
            user_config=app_context.user_config,
        )

        self._save_components_and_config(new_app_context)

        return new_app_context
          

    def edit_user_config(
        self,
        app_context: AppContext
    ) -> AppContext:
        user_config: UserConfig = app_context.user_config

        #select user_config
        request_for_user_config: EditRequest = self._interface_adapter.select_change(user_config)

        #restore AppContext from EditRequest
        new_user_config = cast(
            UserConfig,
            self._replace_path_following_to_edit_request(
                obj=user_config,
                path=request_for_user_config.path,
                #user_configは値がstrなので、.selected_nameのままでいい。
                value=request_for_user_config.selected_name
            )
        )

        new_app_context = AppContext(
            user_id=app_context.user_id,
            components=app_context.components,
            user_config=new_user_config
        )

        #save changed user_config
        self._save_components_and_config(new_app_context)
        
        return new_app_context

 
    def _replace_path_following_to_edit_request(
        self,
        obj,
        path: tuple[str, ...],
        value: object
    ):
        if len(path) == 1:
            return replace(obj, **{path[0]: value})

        child = getattr(obj, path[0])

        new_child = self._replace_path_following_to_edit_request(
            child,
            path[1:],
            value,
        )

        return replace(
            obj,
            **{path[0]: new_child},
        )



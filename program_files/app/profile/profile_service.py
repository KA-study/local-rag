from dataclasses import replace, fields
from typing import cast

from program_files.app.context.context import AppContext
from program_files.app.context.components import Components
from program_files.app.context.user_config import UserConfig
from program_files.app.registry.components_registry import ComponentsRegistry
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



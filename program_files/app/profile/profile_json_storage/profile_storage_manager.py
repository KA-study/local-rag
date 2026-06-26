from dataclasses import is_dataclass, fields
import json

from program_files.app.profile.profile_json_storage._types import PROFILE_PATH
from program_files.app.context.context import AppContext
from program_files.app.context.components import Components
from program_files.app.context.user_config import UserConfig
from program_files.app.registry.components_registry import ComponentsRegistry


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
        
        app_context_dict = self._app_context_to_json(app_context)

        # 既存データ読み込み
        if PROFILE_PATH.exists():
            with open(PROFILE_PATH, "r", encoding="utf-8") as f:
                profiles = json.load(f)
        else:
            profiles = {}

        # ユーザー情報更新
        profiles[app_context.user_id] = app_context_dict

        # 保存
        with open(PROFILE_PATH, "w", encoding="utf-8") as f:
            json.dump(
                profiles,
                f,
                ensure_ascii=False,
                indent=4,
            )


    def _json_to_app_context(
        self,
        json: dict
    ) -> AppContext:
        ...


    def _app_context_to_json(
        self,
        app_context: AppContext
    ) -> dict:
        components: Components = app_context.components
        user_config: UserConfig = app_context.user_config

        components_dict = self._components_to_json(components)
        user_config_dict = self._user_config_to_json(user_config)

        app_context_dict = {
            "components": components_dict,
            "user_config": user_config_dict,
        }

        return app_context_dict


    def _components_to_json(
        self,
        obj,
    ):
        #枝部分処理
        if is_dataclass(obj):
            return {
                field.name: self._components_to_json(
                    getattr(obj, field.name)
                )
                for field in fields(obj)
            }

        #葉部分処理
        if isinstance(obj, type):
            return ComponentsRegistry.get_name(obj)

        raise TypeError(
            f"Unsupported type in Components: {type(obj).__name__}"
        )


    def _user_config_to_json(
        self,
        obj,
    ):
        #枝部分処理
        if is_dataclass(obj):
            return {
                field.name: self._user_config_to_json(
                    getattr(obj, field.name)
                )
                for field in fields(obj)
            }

        #葉部分処理
        return obj



"""
保存辞書イメージ

{
    user_1: {
        components: {
            session_components: {
                history_db:  str
                },
            passive_components: {
                embedder: str,
                vector_store: str,
                ...
                },
            ...
        },
        user_config: {
            ...
        }
    },

    user_2: {
        ...
    },
    ...
}
"""

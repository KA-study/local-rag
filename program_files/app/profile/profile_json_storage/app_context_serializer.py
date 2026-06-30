from typing import cast
from dataclasses import fields, is_dataclass

from program_files.app.context.context import AppContext
from program_files.app.context.components import Components
from program_files.app.context.user_config import UserConfig
from program_files.app.registry.components_registry import ComponentsRegistry


class AppContextSerializer:

    def dict_to_app_context(
        self,
        app_context_dict: dict
    ) -> AppContext:

        components_dict = app_context_dict["components"]
        user_config_dict = app_context_dict["user_config"]

        components = self._dict_to_components(components_dict)
        user_config = self._dict_to_user_config(user_config_dict)

        app_context = AppContext(
            components = cast(
                Components,
                components
            ),
            user_config = cast(
                UserConfig,
                user_config
            ),
        )


        return app_context


    def _dict_to_components(
        self,
        data,
        cls: type = Components,
    ):
        #枝部分処理
        if is_dataclass(cls):
            return cls(**{
                field.name: self._dict_to_components(
                    data[field.name],
                    #field.typeにstrなどが入ることはない。
                    cast(
                        type,
                        field.type
                    ),
                )
                for field in fields(cls)
            })

        #葉部分処理
        for base in ComponentsRegistry._registry:
            try:
                return ComponentsRegistry.get_type(base, data)
            except ValueError:
                pass

        raise ValueError(f"Unknown component: {data}")


    def _dict_to_user_config(
        self,
        data,
        cls: type = UserConfig,
    ):
        if is_dataclass(cls):
            return cls(**{
                field.name: self._dict_to_user_config(
                    data[field.name],
                    #field.typeにstrなどが入ることはない。
                    cast(
                        type,
                        field.type
                    ),
                )
                for field in fields(cls)
            })
    
        return data


    def app_context_to_dict(
        self,
        app_context: AppContext
    ) -> dict:
        components: Components = app_context.components
        user_config: UserConfig = app_context.user_config

        components_dict = self._components_to_dict(components)
        user_config_dict = self._user_config_to_dict(user_config)

        app_context_dict = {
            "components": components_dict,
            "user_config": user_config_dict,
        }

        return app_context_dict

 
    def _components_to_dict(
        self,
        obj,
    ):
        #枝部分処理
        if is_dataclass(obj):
            return {
                field.name: self._components_to_dict(
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


    def _user_config_to_dict(
        self,
        obj,
    ):
        #枝部分処理
        if is_dataclass(obj):
            return {
                field.name: self._user_config_to_dict(
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


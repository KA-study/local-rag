import json

from program_files.app.profile.profile_json_storage._types import PROFILE_PATH
from program_files.app.context.context import AppContext
from program_files.app.profile.profile_json_storage.app_context_serializer import AppContextSerializer


class ProfileStorageManager:

    def __init__(self):
        self._app_context_serializer = AppContextSerializer()

    def load(
        self,
        user_id: str
    ) -> AppContext:

        if not PROFILE_PATH.exists():
            raise FileNotFoundError("Profile file does not exist.")

        #自動的に閉じる
        with open(PROFILE_PATH, "r", encoding="utf-8") as f:
            profiles: dict = json.load(f)

        try:
            json_data = profiles[user_id]
        except KeyError:
            raise KeyError(f"User '{user_id}' not found.")

        return self._app_context_serializer.dict_to_app_context(json_data)


    def save(
        self,
        app_context: AppContext
    ) -> None:
        
        app_context_dict = self._app_context_serializer.app_context_to_dict(app_context)

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

    
    def get_all_app_context(self) -> list[AppContext]:
 
        if PROFILE_PATH.exists():
            with open(PROFILE_PATH, "r", encoding="utf-8") as f:
                profiles = json.load(f)
        else:
            raise ValueError("no user_id is registered.")

        app_context_list = [AppContext()]

        for profile in profiles:
            app_context_list.append(self._app_context_serializer.dict_to_app_context(profile))

        return app_context_list

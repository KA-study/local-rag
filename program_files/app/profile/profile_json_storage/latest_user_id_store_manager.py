import json

from program_files.app.profile.profile_json_storage._types import LATEST_USER_ID_STORE_PATH


class LatestUserIdStoreManager:

    def load(self) -> str:
        ...

    def save(
        self,
        user_id: str
    ) -> None:
        ...

       
"""
保存形式は、str、単一のuser_idのみ。常に一つのuser_idのみが入る形。log化はまだしない。
"""

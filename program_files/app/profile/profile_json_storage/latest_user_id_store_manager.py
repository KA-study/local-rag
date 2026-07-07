import json

from program_files.shared.config import LATEST_USER_ID_STORE_PATH


class LatestUserIdStoreManager:

    def load(self) -> str:

        if not LATEST_USER_ID_STORE_PATH.exists():
            raise FileNotFoundError("Latest user ID store does not exist.")

        with open(LATEST_USER_ID_STORE_PATH, "r", encoding="utf-8") as f:
            data: dict[str, str] = json.load(f)

        try:
            return data["user_id"]
        except KeyError:
            raise KeyError("'user_id' does not exist.")


    def save(
        self,
        user_id: str
    ) -> None:

        data = {
            "user_id": user_id,
        }

        with open(LATEST_USER_ID_STORE_PATH, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4,
            )
       
"""
保存形式は、
{
    "user_id": str,
}
"""

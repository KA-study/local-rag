from typing import Protocol

class SessionManagerInterface(Protocol):

    #セッション一覧および新規セッションの選択肢を表示し、選択を受け取る
    def select_session(
        self,
        session_ids: list[str]
    ) -> str:
        ...



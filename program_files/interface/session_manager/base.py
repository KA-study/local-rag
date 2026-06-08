from typing import Protocol

from program_files.shared.schemas import ExitCommandError

class SessionManagerInterface(Protocol):

    #セッション一覧および新規セッションの選択肢を表示し、選択を受け取る
    def select_session_id(
        self,
        session_ids: list[str]
    ) -> str:
        ...

    def create_session_id(self) -> str:
        ...

    def _check_exit(self, user_input):
        ...


from abc import ABC, abstractmethod

from program_files.interface.base.base_interface import Interface


class SessionManagerInterface(Interface, ABC):

    #セッション一覧および新規セッションの選択肢を表示し、選択を受け取る
    @abstractmethod
    def select_session_id(
        self,
        session_ids: list[str]
    ) -> str:
        ...

    @abstractmethod
    def create_session_id(self) -> str:
        ...



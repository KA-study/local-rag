

from active.session._types import SessionContext
from interface.session_manager.base import SessionManagerInterface


class SessionManagerInterfaceAdapter:

    def __init__(
        self,
        session_manager_interface: SessionManagerInterface
    ):
        self._s_m_interface = session_manager_interface


    def select_session(
        self,
        session_contexts: list[SessionContext]
    ) -> SessionContext:

        session_ids: list[str] = [
            session_context.session_id
            for session_context in session_contexts
        ]

        session_id: str = self._s_m_interface.select_session(session_ids)

        #session_id == "_NEW_"だった時の処理
        if session_id == "_NEW_":
           ... 


        session_context = SessionContext(session_id=session_id)

        return session_context



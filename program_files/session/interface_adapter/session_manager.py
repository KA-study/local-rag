

from program_files.session._types import SessionContext
from program_files.runtime import Runtime


class SessionManagerInterfaceAdapter:

    def __init__(
        self,
    ):
        self._s_m_interface = Runtime.get_interface().session_manager()


    def select_session(
        self,
        session_contexts: list[SessionContext]
    ) -> SessionContext:

        session_ids: list[str] = [
            session_context.session_id
            for session_context in session_contexts
        ]

        session_id: str = self._s_m_interface.select_session_id(session_ids)

        #session_id == "_NEW_"だった時の処理
        if session_id == "_NEW_":
            session_id: str = self._s_m_interface.create_session_id()

        session_context = SessionContext(session_id=session_id)

        return session_context


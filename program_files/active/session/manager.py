#ここでSessionを呼ぶ

from active.session.session import Session

class SessionManager:

    def create(self) -> Session:
        ...

    def save(self, session: Session):
        ...

    def load(
        self,
        session_id: str
    ) -> Session:
        ...

    def list_sessions(self):
        ...

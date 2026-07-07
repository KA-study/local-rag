#ここでSessionを呼ぶ
#ここでhistory_managerをインスタンス化する

from program_files.app.context.context import AppContext
from program_files.session.session import Session
from program_files.session.history.history_manager import HistoryManager
from program_files.session.interface_adapter.session_manager import SessionManagerInterfaceAdapter
from program_files.session._types import SessionContext
from program_files.shared.schemas import ExitCommandError
from program_files.shared.manager_interface import Manager

#過去のセッション、または新規セッションを選択できる画面（Lineでいう、フレンド一覧画面）を提供し、またそのうちのいづれかが選択されたとき、Sessionクラス内の処理に移る。

"""
セッション一覧取得

セッション一覧および新規作成を表示

セッション選択入力待機

選択されたセッションでsession.run()

コマンド確認（SessionManager終了）
"""
class SessionManager(Manager):

    def __init__(
        self,
        app_context: AppContext
    ):
        self._app_context = app_context
        self._history_manager = HistoryManager(app_context)
        #このcliとguiの切り替えは、後ほどよく考えて再実装
        self._s_m_interface_adapter = SessionManagerInterfaceAdapter()


    def name(self) -> str:
        return "start_session"

    
    def run(self, app_context: AppContext):
    
        while True:

            #セッション一覧取得
            session_contexts: list[SessionContext] = self._history_manager.get_session_contexts()

            #セッション一覧および新規作成を表示し、選択されたsessionを取得
            #SessionManagerブロックを抜け出す処理
            try:
                session_context: SessionContext = self._s_m_interface_adapter.select_session(session_contexts)
            except ExitCommandError:
                break
            
            #選択されたsessionでsession.run()
            session = Session(
                app_context=self._app_context,
                session_context=session_context,
                history_manager=self._history_manager,
            )

            #ここに、各sessionが終了したときの処理
            session.run()



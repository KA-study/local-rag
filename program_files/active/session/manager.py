#ここでSessionを呼ぶ
#ここでhistory_managerをインスタンス化する

from active.session.session import Session
from active.session.history.history_manager import HistoryManager
from active.session._types import SessionContext
from app.context import AppContext

#過去のセッション、または新規セッションを選択できる画面（Lineでいう、フレンド一覧画面）を提供し、またそのうちのいづれかが選択されたとき、Sessionクラス内の処理に移る。

"""
セッション一覧取得

セッション一覧および新規作成を表示

セッション選択入力待機

選択されたセッションでsession.run()

コマンド確認（SessionManager終了）
"""
class SessionManager:

    def __init__(
        self,
        app_context: AppContext
    ):
        self._app_context = app_context

    
    def run(self):
    
        while True:

            #セッション一覧取得



from app.context import AppContext
from active.session.history.history_manager import HistoryManager
from active.session._types import SessionContext
from active.query.pipeline import QueryPipeline
from active._types import Message
from interface.chat.base import ChatInterface

class Session:

    #Sessionインスタンス化時に、CliInterfaceを引数として渡して初めて、Protocolの静的チェックが効く。
    #session開始時（このクラスがインスタンス化されたとき）historyを見て、あったらそれをすべて表示する。
    def __init__(
        self,
        app_context: AppContext,
        session_context: SessionContext,
        history_manager: HistoryManager,
        ui: ChatInterface
    ):

        self._session_context = session_context
        self._pipeline = QueryPipeline(app_context, history_manager)
        self._ui: ChatInterface = ui
        self._app_context = app_context

        self._history_manager = history_manager

    def run(self):
    
        while True:

            #入力
            query: str = self._ui.get_input()

            #入力に意味付け
            message = Message(role="user", content=query)

            #QueryPipeline
            assistant_output: Message = self._pipeline.run(
                    message
                )

            #出力
            self._ui.display_message(
                role=assistant_output.role,
                text=assistant_output.content
            )

            #履歴変更（history）
            self._history_manager.save_history(
                message,
                self._session_context
            )

            #コマンド確認（session終了）





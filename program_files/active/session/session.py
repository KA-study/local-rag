
from program_files.app.context import AppContext
from program_files.active.session.history.history_manager import HistoryManager
from program_files.active.session._types import SessionContext
from program_files.active.session.interface_adapter.chat import ChatInterfaceAdapter
from program_files.active.query.pipeline import QueryPipeline
from program_files.active._types import Message
from program_files.interface.chat.base import ChatInterface
from program_files.shared.schemas import ExitCommandError

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
        self._ui = ChatInterfaceAdapter(ui)
        self._app_context = app_context

        self._history_manager = history_manager

    def run(self):
    
        while True:

            #入力
            #:qが実行されたとき、ここにエラーが出て、上でそれをハンドリング
            try:
                message: Message = self._ui.get_input()
            except ExitCommandError:
                break

            #QueryPipeline
            assistant_output: Message = self._pipeline.run(message)

            #出力
            self._ui.display_message(assistant_output)

            #履歴変更（history）
            self._history_manager.save_history(
                message,
                self._session_context
            )






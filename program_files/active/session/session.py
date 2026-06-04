
from app.context import AppContext
from active.session.history import History
from active.query.pipeline import QueryPipeline
from active._types import Message
from interface.chat.base import ChatInterface

class Session:

    #Sessionインスタンス化時に、CliInterfaceを引数として渡して初めて、Protocolの静的チェックが効く。
    def __init__(
        self,
        app_context: AppContext,
        session_id: str,
        history: History,
        ui: ChatInterface
    ):

        self._session_id = session_id
        self._history = history
        self._pipeline = QueryPipeline(app_context)
        self._ui: ChatInterface = ui
        self._app_context = app_context


    def run(self):
    
        while True:

            #入力
            query: str = self._ui.get_input()

            #入力に意味付け
            message = Message(role="user", content=query)

            #QueryPipeline
            assistant_output: Message = self._pipeline.run(
                    message,
                    self._history,
                )

            #出力
            self._ui.display_message(assistant_output.content)

            #履歴変更（history）

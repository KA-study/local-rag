
from app.context import AppContext
from active.session.history import History
from active.query.pipeline import QueryPipeline
from active.ui.base import UserInterface

class Session:

    #Sessionインスタンス化時に、CliInterfaceを引数として渡して初めて、Protocolの静的チェックが効く。
    def __init__(
        self,
        app_context: AppContext,
        session_id: str,
        history: History,
        ui: UserInterface
    ):

        self._session_id = session_id
        self._history = history
        self._pipeline = QueryPipeline(app_context)
        self._ui = ui
        self._app_context = app_context


    def run(self):
    
        while True:

            #入力
            query: str = self._ui.get_input()

            #QueryPipeline

            #出力

            #履歴変更

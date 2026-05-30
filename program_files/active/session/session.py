
from active.session.history import History
from active.query.pipeline import QueryPipeline

class Session:

    def __init__(
        self,
        session_id: str,
        history: History,
        pipeline: QueryPipeline
    ):

        self._session_id = session_id
        self._history = history
        self._pipeline = pipeline


    def run(self):
    
        while True:
            ...
    
            #入力

            #検索

            #生成

            #出力

            #履歴変更

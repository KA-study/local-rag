#質問一回分を処理
from active.session.history import History

class QueryPipeline:

    def run(
        self,
        query: str,
        history: History
    ) -> str:
        ...

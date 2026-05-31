#プロンプト生成
from active.session.history import History
from shared.schemas import RetrievedChunk

class PromptBuilder:

    def build(
        self,
        query: str,
        history: History,
        chunks: list[RetrievedChunk]
    ) -> str:
        ...

#プロンプト生成
from active.session.history import History
from shared.schemas import RetrievedChunk

class PromptBuilder:
    TEMPLATE = """
        ### Context
        {context}

        ### History
        {history}

        ### Question
        {query}

        ### Answer
    """.strip()


    def build(
        self,
        query: str,
        history: History,
        context: str
    ) -> str:

        return self.TEMPLATE.format(
            query=query,
            history=history,
            context=context,
        )    

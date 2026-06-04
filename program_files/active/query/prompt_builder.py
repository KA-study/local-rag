#プロンプト生成
from active.session.history import History
from active._types import Message

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
        message: Message,
        history: History,
        context: str
    ) -> str:

        query = message.content

        history_str = history.to_prompt()

        return self.TEMPLATE.format(
            query=query,
            history=history_str,
            context=context,
        )    

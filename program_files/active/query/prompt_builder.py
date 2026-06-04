#プロンプト生成
from active.session.history.history_manager import HistoryManager
from active._types import Message

class PromptBuilder:

    def __init__(self, history_manager: HistoryManager):
        self._history_manager = history_manager

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
        context: str
    ) -> str:

        query = message.content

        messages: list[Message] | None = self._history_manager.load_history()

        if messages is None:
            history_str = ""

        else:
            str_message_list: list[str] = [
                    f"{message.role}: {message.content}" for message in messages
            ]

            history_str: str = "\n".join(str_message_list)

        return self.TEMPLATE.format(
            query=query,
            history_str=history_str,
            context=context,
        )    

#プロンプト生成
from program_files.active.session.history.history_manager import HistoryManager
from program_files.active.session._types import SessionContext
from program_files.active._types import Message
from program_files.active.session._types import SessionContext

class PromptBuilder:

    def __init__(
        self,
        session_context: SessionContext,
        history_manager: HistoryManager,
    ):
        self._session_context = session_context
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


#過去のchat履歴と今回の送信文を組み合わせてプロンプトを作る
    def build(
        self,
        message: Message,
        context: str,
    ) -> str:

        query = message.content

        messages: list[Message] | None = self._history_manager.load_history(self._session_context)

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

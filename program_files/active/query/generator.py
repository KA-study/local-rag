#クエリジェネレーター
from active._types import Message

class QueryGenerator:

    def generate(self, message: Message) -> Message:
        message.content.strip()

        return message

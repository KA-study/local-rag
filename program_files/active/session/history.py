from active._types import Message

#Historyはsessionごとにインスタンスがあるはず
class History:

    def __init__(self) -> None:
        self._messages: list[Message] = []

    def to_prompt(self) -> str:
        return "\n".join(
            f"{h.role}: {h.content}\n"
            for h in self._messages
        )



from program_files.runtime import Runtime
from program_files.session._types import Message


class ChatInterfaceAdapter:

    def __init__(
        self,
    ):
        self._chat_interface = Runtime.get_interface().chat() 

    
    def get_input(self) -> Message:
        
        content: str = self._chat_interface.get_input()

        return Message(
            role="user",
            content=content
        )
        

    def display_message(
        self,
        message: Message
    ) -> None:

        role = message.role
        content = message.content

        self._chat_interface.display_message(
            role,
            content
        )

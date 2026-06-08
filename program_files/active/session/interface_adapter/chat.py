

from program_files.interface.chat.base import ChatInterface
from program_files.active._types import Message


class ChatInterfaceAdapter:

    def __init__(
        self,
        chat_interface: ChatInterface
    ):
        self._chat_interface = chat_interface 

    
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

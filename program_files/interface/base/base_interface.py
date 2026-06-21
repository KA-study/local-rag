from abc import ABC
from typing import final

from program_files.shared.schemas import ExitCommandError


class Interface(ABC):

    @final
    def _input(self, *arguments: object) -> str:

        prompt = "".join(map(str, arguments))

        user_input = input(prompt)

        if user_input == ":q":
            raise ExitCommandError()

        return user_input

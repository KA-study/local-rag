from typing import Protocol

from program_files.shared.schemas import LLMResponse

class LLM(Protocol):
    def generate(self, prompt: str) -> LLMResponse:
        '''
        promptを受け取り、LLMの出力を返す。
        '''
        ...


from typing import Protocol

class LLM(Protocol):
    def generate(self, prompt: str) -> str:
        '''
        promptを受け取り、LLMの出力を返す。
        '''
        ...

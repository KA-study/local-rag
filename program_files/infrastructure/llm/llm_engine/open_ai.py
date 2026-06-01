from openai import OpenAI

from infrastructure.llm.base import LLM

#呼び出し側は、open_ai: LLM = OpenAILLM　とすることで、protocolを有効化すること。
class OpenAILLM:
    
    def __init__(self, model: str = "gpt-4.1-mini"):
        self.client = OpenAI()
        self.model = model

    def generate(self, prompt: str) -> str:

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        return response.output_text


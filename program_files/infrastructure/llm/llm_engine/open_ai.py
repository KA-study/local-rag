from openai import OpenAI

from shared.schemas import LLMResponse
from shared.schemas import Usage

#呼び出し側は、open_ai: LLM = OpenAILLM　とすることで、protocolを有効化すること。
#OpenAI の特殊型はこのクラス内に完全に閉じ込める。
class OpenAILLM:
    
    def __init__(self, model: str = "gpt-4.1-mini"):
        self.client = OpenAI()
        self.model = model


    def generate(self, prompt: str) -> LLMResponse:

        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )

        if response.usage is None:
            usage = None
        else:
            usage = Usage(
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
                model_name=self.model
            )

        return LLMResponse(
            text=response.output_text,
            model=self.model,
            usage=usage
        )



from program_files.app.registry.components_registry import ComponentsRegistry
from program_files.shared.schemas import LLMResponse, Usage
from program_files.infrastructure.llm.llm_engine.base import LLM


@ComponentsRegistry.component(
    base=LLM,
    name="fake_llm"
)
class FakeLLM(LLM):

    def generate(self, prompt: str) -> LLMResponse:

        usage = Usage(
            input_tokens=0,
            output_tokens=0,
            model_name="gake"
        )
        
        return LLMResponse(
            text=f"You are useing FakeLLM. prompt is '{prompt}'",
            model="fake",
            usage=usage
        )

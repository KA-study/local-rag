
from program_files.infrastructure.llm.llm_engine.open_ai import OpenAILLM
from program_files.infrastructure.llm.llm_engine.fake_llm import FakeLLM
from program_files.infrastructure.llm.cost.cost_manager import CostManager
from program_files.app.context.context import AppContext
from program_files.shared.schemas import LLMResponse

class LLMManager:

    def __init__(
        self,
        app_context: AppContext
    ):
        self._app_context = app_context
        #ここは一旦固定だが、最終的には上層部でまとめて管理し、引数として受け取る形にする。
        self.llm = FakeLLM()
        self.cost_manager = CostManager(app_context)


    def generate(self, prompt: str) -> str:
        #  事前チェック（必要なら）
        try:
            self.cost_manager.check_allowance()
        except ValueError:
            #コスト超過時は、エラーを送出し、ここでハンドリング。
            raise

        #  実行
        res: LLMResponse = self.llm.generate(prompt)

        #  usageがある場合のみコスト加算
        if res.usage is not None:
            self.cost_manager.write_log_and_status(res.usage)

        return res.text

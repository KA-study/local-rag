
from infrastructure.llm.llm_engine.open_ai import OpenAILLM
from infrastructure.llm.cost.cost_manager import CostManager

class LLMManager:

    def __init__(
        self
    ):
        #ここは一旦固定だが、最終的には上層部でまとめて管理し、引数として受け取る形にする。
        self.llm = OpenAILLM()
        self.cost_manager = CostManager()
        self.model_name = "gpt-4.1-mini"


    def generate(self, prompt: str) -> str:
        #  事前チェック（必要なら）
        try:
            self.cost_manager.check_allowance()
        except:
            #コスト超過時は、エラーを送出し、ここでハンドリング。
            ...

        #  実行
        res = self.llm.generate(prompt)

        #  usageがある場合のみコスト加算
        #ここでmodel_name渡す
        if res.usage is not None:
            ...

        return res.text

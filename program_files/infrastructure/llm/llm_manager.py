
from infrastructure.llm.llm_engine.open_ai import OpenAILLM
from infrastructure.llm.cost.cost_manager import CostManager

class LLMManager:

    def __init__(
        self
    ):
        #ここは一旦固定だが、最終的には上層部でまとめて管理し、引数として受け取る形にする。
        self.llm = OpenAILLM()
        self.cost_manager = CostManager()


    def generate(self, prompt: str) -> str:
        #  事前チェック（必要なら）
        try:
            self.cost_manager.check_allowance(prompt)
        except:
            #コスト超過時は、エラーを送出し、ここでハンドリング。
            ...

        #  実行
        res = self.llm.generate(prompt)

        #  usageがある場合のみコスト加算
        if res.usage is not None:
            self.cost_manager.add_usage(res.usage)

        return res.text

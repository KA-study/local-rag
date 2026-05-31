#質問一回分を処理

'''
QueryPipeline.runはオーケストレーター


検索クエリ生成

Retriever

関連チャンク生成

PromptBuilder

最終プロンプト生成

LLMClient

解答
'''

from active.session.history import History
from active.query.generator import QueryGenerator
from active.query.retriever import Retriever
from active.query.prompt_builder import PromptBuilder
from infrastructure.llm.client import LLMClient

class QueryPipeline:

    def __init__(self):
        self._query_generator = QueryGenerator()
        self._retriever = Retriever()
        self._prompt_builder = PromptBuilder()
        self._llm_client = LLMClient()

    def run(
        self,
        query: str,
        history: History
    ) -> str:
        '''
        質問一回分を処理
        '''

        #検索クエリ生成
        aearch_query = self._query_generator.generate(query)


#質問一回分を処理
'''
QueryPipeline.runはオーケストレーター


検索クエリ生成

Retriever：検索クエリに対して、関連チャンクを集める。

関連チャンク生成

PromptBuilder

最終プロンプト生成

LLMClient

解答
'''

from active.session.history import History
from active.query.generator import QueryGenerator
from active.query.retriever import Retriever
from active.query.context_builder import ContextBuilder
from active.query.prompt_builder import PromptBuilder
from infrastructure.llm.client import LLMClient
from infrastructure.vector_store.chroma_store import ChromaVectorStore
from shared.schemas import RetrievedChunk

class QueryPipeline:

    def __init__(self):
        #ここは後ほど上から持ってこれるようにする。
        self._query_generator = QueryGenerator()
        self._retriever = Retriever()
        self._prompt_builder = PromptBuilder()
        self._llm_client = LLMClient()
        self._context_builder = ContextBuilder()

    def run(
        self,
        query: str,
        history: History
    ) -> str:
        '''
        質問一回分を処理
        '''

        #検索クエリ生成
        generated_query: str = self._query_generator.generate(query)

        #Retrieve
        retrieved_chunks: list[RetrievedChunk] = self._retriever.retrieve(generated_query)

        #Context生成
        context_str: str = self._context_builder.build(retrieved_chunks)

        #Prompt生成        
        prompt_str: str = self._prompt_builder.build(generated_query, history, context_str)

















#質問一回分を処理
'''
QueryPipeline.runはオーケストレーター


検索クエリ生成

Retriever：検索クエリに対して、関連チャンクを集める。

関連チャンク生成

PromptBuilder

最終プロンプト生成

LLMClient

LLMOutputをデータ化

解答
'''

from active.session.history import History
from active.query.generator import QueryGenerator
from active.query.retriever import Retriever
from active.query.context_builder import ContextBuilder
from active.query.prompt_builder import PromptBuilder
from active._types import Message
from infrastructure.llm.llm_manager import LLMManager
from shared.schemas import RetrievedChunk
from app.context import AppContext

class QueryPipeline:

    def __init__(self, app_context: AppContext):
        self._app_context = app_context
        #ここは後ほど上から持ってこれるようにする。
        self._query_generator = QueryGenerator()
        self._retriever = Retriever()
        self._prompt_builder = PromptBuilder()
        self._llm_manager = LLMManager(app_context)
        self._context_builder = ContextBuilder()

    def run(
        self,
        message: Message,
        history: History
    ) -> Message:
        '''
        質問一回分を処理
        '''

        #検索クエリ生成
        generated_message: Message = self._query_generator.generate(message)

        #Retrieve
        retrieved_chunks: list[RetrievedChunk] = self._retriever.retrieve(generated_message)

        #Context生成
        context_str: str = self._context_builder.build(retrieved_chunks)

        #Prompt生成        
        prompt_str: str = self._prompt_builder.build(generated_message, history, context_str)

        #LLM処理
        llm_response: str = self._llm_manager.generate(prompt_str)

        #LLM Response 意味付け
        llm_message = Message(role="assistant", content=llm_response)

        return llm_message

















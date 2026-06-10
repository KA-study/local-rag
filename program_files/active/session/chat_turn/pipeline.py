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

from program_files.active.session.history.history_manager import HistoryManager
from program_files.active.session.chat_turn.generator import QueryGenerator
from program_files.active.session.chat_turn.retriever import Retriever
from program_files.active.session.chat_turn.context_builder import ContextBuilder
from program_files.active.session.chat_turn.prompt_builder import PromptBuilder
from program_files.active._types import Message
from program_files.infrastructure.llm.llm_manager import LLMManager
from program_files.shared.schemas import RetrievedChunk
from program_files.app.context import AppContext

class QueryPipeline:

    def __init__(
        self,
        app_context: AppContext,
        history_manager: HistoryManager
    ):
        self._app_context = app_context
        #ここは後ほど上から持ってこれるようにする。
        self._query_generator = QueryGenerator()
        self._retriever = Retriever()
        self._prompt_builder = PromptBuilder(history_manager)
        self._llm_manager = LLMManager(app_context)
        self._context_builder = ContextBuilder()

    def run(
        self,
        message: Message
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
        prompt_str: str = self._prompt_builder.build(
            generated_message,
            context_str
        )

        #LLM処理
        llm_response: str = self._llm_manager.generate(prompt_str)

        #LLM Response 意味付け
        llm_message = Message(role="assistant", content=llm_response)

        return llm_message

















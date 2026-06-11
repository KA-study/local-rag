from typing import TypedDict

from program_files.session.history.history_db import SQliteHistoryDB
from program_files.passive.pdf.loader import PypdfLoader
from program_files.passive.pdf.chunker import TokenChunker
from program_files.interface.chat.cli import CliChatInterface
from program_files.interface.session_manager.cli import SessionManagerInterface
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from program_files.infrastructure.llm.llm_engine.fake_llm import FakeLLM
from program_files.infrastructure.llm.llm_engine.open_ai import OpenAILLM
from program_files.infrastructure.llm.cost.usage_db import SQliteUsageDB
from program_files.infrastructure.embedding.embedder import STEmbedder

#Active
class HISTORY_DB_MAPPER(TypedDict):
    sqlite_history_db: SQliteHistoryDB

#Passive
class PDF_LOADER_MAPPER(TypedDict):
    py_pdf_loader: PypdfLoader

class CHUNKER_MAPPER(TypedDict):
    token_chunker: TokenChunker

#Interface
class CHAT_INTERFACE_MAPPER(TypedDict):
    cli_chat_interface: CliChatInterface

class SESSION_MANAGER_INTERFACE_MAPPER(TypedDict):
    cli_session_manager_interface: SessionManagerInterface

#Infrastructure
class VECTOR_STORE_MAPPER(TypedDict):
    chroma_vector_store: ChromaVectorStore

class LLM_ENGINE_MAPPER(TypedDict):
    open_ai_llm: OpenAILLM
    fake_llm: FakeLLM

class USAGE_DB_MAPPER(TypedDict):
    sqlite_usage_db: SQliteUsageDB

class EMBEDDER_MAPPER(TypedDict):
    st_embedder: STEmbedder

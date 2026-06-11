from program_files.app.settings import (
    Components,
    SessionComponents,
    PassiveComponents,
    InterfaceComponents,
    InfrastructureComponents,
)
from program_files.session.history.history_db import HistoryDB
from program_files.passive.pdf.loader import PypdfLoader
from program_files.passive.pdf.chunker import TokenChunker
from program_files.interface.chat.cli import CliChatInterface
from program_files.interface.session_manager.cli import CliSessionManagerInterface
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from program_files.infrastructure.llm.llm_engine.fake_llm import FakeLLM
from program_files.infrastructure.llm.cost.usage_db import UsageDB
from program_files.infrastructure.embedding.embedder import STEmbedder


DEFAULT_USER_ID: str = "default"


DEFAULT_SESSION_COMPONENTS = SessionComponents(
    history_db=HistoryDB
)

DEFAULT_PASSIVE_COMPONENTS = PassiveComponents(
    pdf_loader=PypdfLoader,
    chunker=TokenChunker,
)

DEFAULT_INTERFACE_COMPONENTS = InterfaceComponents(
    chat_interface=CliChatInterface,
    session_manager_interface=CliSessionManagerInterface
)

DEFAULT_INFRASTRUCTURE_COMPONENTS = InfrastructureComponents(
    vector_store=ChromaVectorStore,
    llm_engine=FakeLLM,
    usage_db=UsageDB,
    embedder=STEmbedder,
)

DEFAULT_COMPONENTS = Components(
    session=DEFAULT_SESSION_COMPONENTS,
    passive=DEFAULT_PASSIVE_COMPONENTS,
    interface=DEFAULT_INTERFACE_COMPONENTS,
    infrastructure=DEFAULT_INFRASTRUCTURE_COMPONENTS,
)

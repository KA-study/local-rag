from program_files.app.components import (
    Components,
    SessionComponents,
    PassiveComponents,
    InterfaceComponents,
    InfrastructureComponents,
)
from program_files.app.user_config import (
    Path,
    UserConfig
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

#============user_id=========================

DEFAULT_USER_ID: str = "default"

#============components======================

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

#===========user_config=========================

DEFAULT_PDF_PATH = "default.pdf"

DEFAULT_HISTORY_DB_PATH = "history.db"

DEFAULT_USAGE_DB_PATH = "usage.db"


DEFAULT_PATH = Path(
    pdf=DEFAULT_PDF_PATH,
    history_db=DEFAULT_HISTORY_DB_PATH,
    usage_db=DEFAULT_USAGE_DB_PATH,
)

DEFAULT_USER_CONFIG = UserConfig(
    path=DEFAULT_PATH,
)



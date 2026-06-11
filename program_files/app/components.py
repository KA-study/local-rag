from dataclasses import dataclass

from program_files.session.history.base import HistoryDB
from program_files.passive.pdf.base import (
    PDFLoaderBase,
    PDFChunkerBase
)
from program_files.interface.chat.base import ChatInterface
from program_files.interface.session_manager.base import SessionManagerInterface
from program_files.infrastructure.embedding.base import BaseEmbedder
from program_files.infrastructure.llm.llm_engine.base import LLM
from program_files.infrastructure.vector_store.base import VectorStore
from program_files.infrastructure.llm.cost.base import UsageDB


@dataclass
class SessionComponents:
    history_db: type[HistoryDB]

    def __post_init__(self):
        if not issubclass(self.history_db, HistoryDB):
            raise TypeError(
                "history_db must be subclass of HistoryDB."
            )

@dataclass
class PassiveComponents:
    pdf_loader: type[PDFLoaderBase]
    chunker: type[PDFChunkerBase]

    def __post_init__(self):
        if not issubclass(self.pdf_loader, PDFLoaderBase):
            raise TypeError(
                "pdf_loader must be subclass of PDFLoaderBase."
            )
        if not issubclass(self.chunker, PDFChunkerBase):
            raise TypeError(
                "chunker must be subclass of PDFChunkerBase."
            )

#Protocolで実装しているためsubclassチェックは省略
@dataclass
class InterfaceComponents:
    chat_interface: type[ChatInterface]
    session_manager_interface: type[SessionManagerInterface]

@dataclass
class InfrastructureComponents:
    vector_store: type[VectorStore]
    #Protocolで実装しているためsubclassチェックは省略
    llm_engine: type[LLM]
    usage_db: type[UsageDB]
    embedder: type[BaseEmbedder]

    def __post_init__(self):
        if not issubclass(self.vector_store, VectorStore):
            raise TypeError(
                "vector_store must be subclass of VectorStore."
            )
        if not issubclass(self.usage_db, UsageDB):
            raise TypeError(
                "usage_db must be subclass of UsageDB."
            )
        if not issubclass(self.embedder, BaseEmbedder):
            raise TypeError(
                "embedder must be subclass of BaseEmbedder."
            )


@dataclass 
class Components:
    session: SessionComponents
    passive: PassiveComponents
    interface: InterfaceComponents
    infrastructure: InfrastructureComponents

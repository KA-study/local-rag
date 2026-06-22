from dataclasses import dataclass

from program_files.session.history.base import HistoryDB
from program_files.passive.pdf.base import (
    PDFLoaderBase,
    PDFChunkerBase
)
from program_files.infrastructure.embedding.base import BaseEmbedder
from program_files.infrastructure.llm.llm_engine.base import LLM
from program_files.infrastructure.vector_store.base import VectorStore
from program_files.infrastructure.llm.cost.base import UsageDB

from program_files.session.history.history_db import SQliteHistoryDB
from program_files.passive.pdf.loader import PypdfLoader
from program_files.passive.pdf.chunker import TokenChunker
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from program_files.infrastructure.llm.llm_engine.fake_llm import FakeLLM
from program_files.infrastructure.llm.cost.usage_db import SQliteUsageDB
from program_files.infrastructure.embedding.embedder import STEmbedder


@dataclass(frozen=True)
class SessionComponents:
    history_db: type[HistoryDB] = SQliteHistoryDB

    def __post_init__(self):
        if not issubclass(self.history_db, HistoryDB):
            raise TypeError(
                "history_db must be subclass of HistoryDB."
            )

@dataclass(frozen=True)
class PassiveComponents:
    pdf_loader: type[PDFLoaderBase] = PypdfLoader
    chunker: type[PDFChunkerBase] = TokenChunker

    def __post_init__(self):
        if not issubclass(self.pdf_loader, PDFLoaderBase):
            raise TypeError(
                "pdf_loader must be subclass of PDFLoaderBase."
            )
        if not issubclass(self.chunker, PDFChunkerBase):
            raise TypeError(
                "chunker must be subclass of PDFChunkerBase."
            )

@dataclass(frozen=True)
class InfrastructureComponents:
    vector_store: type[VectorStore] = ChromaVectorStore
    #Protocolで実装しているためsubclassチェックは省略
    llm_engine: type[LLM] = FakeLLM
    usage_db: type[UsageDB] = SQliteUsageDB
    embedder: type[BaseEmbedder] = STEmbedder

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


@dataclass(frozen=True)
class Components:
    session: SessionComponents
    passive: PassiveComponents
    infrastructure: InfrastructureComponents

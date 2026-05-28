from abc import ABC, abstractmethod

from shared.schemas import EmbeddedChunk, RetrievedChunk

class VectorStore(ABC):

    @abstractmethod
    def add(self, chunks: list[EmbeddedChunk]) -> None:
        pass

    @abstractmethod
    def search(
        self,
        query_embedding: list[float],
        top_k: int,
    ) -> list[RetrievedChunk]:
        pass

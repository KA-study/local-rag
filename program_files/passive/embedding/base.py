from abc import ABC, abstractmethod

from shared.schemas import Chunk, EmbeddedChunk

class BaseEmbedder(ABC):
    """
    すべてのembedderが従う抽象クラス
    """
    def __init__(self, **kwards):
        pass

    @abstractmethod
    def embed(self, chunks: list[Chunk]) -> list[EmbeddedChunk]:
        pass

    @abstractmethod
    def embed_batch(self, chunks: list[Chunk]) -> list[EmbeddedChunk]:
        pass

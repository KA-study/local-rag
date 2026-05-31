from abc import ABC, abstractmethod
import numpy

from shared.schemas import Chunk, EmbeddedChunk

class BaseEmbedder(ABC):
    """
    すべてのembedderが従う抽象クラス
    """
    def __init__(self, **kwards):
        pass

    @abstractmethod
    def embed(self, text: str) -> numpy.ndarray:
        pass

    @abstractmethod
    def embed_batch(self, texts: list[str]) -> numpy.ndarray:
        pass

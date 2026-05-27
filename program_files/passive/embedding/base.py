from abc import ABC, abstractmethod

class BaseEmbedder(ABC):
    """
    すべてのembedderが従う抽象クラス
    """
    def __init__(self):
        pass

    @abstractmethod
    def embed(self):
        pass

    def embed_batch(self):
        pass

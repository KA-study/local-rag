from abc import ABC, abstractmethod
from shared.schemas import Document
from pathlib import Path

from shared.schemas import Chunk

#===========PDFLoader=================
class PDFLoaderBase(ABC):
    """
    すべてのPDFローダーが従うインターフェース
    """
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(self.file_path)


    @abstractmethod
    def load_pdf(self) -> list[Document]:
        pass
        
#===========PDFChunker=================
class PDFChunkerBase(ABC):
    """
    すべてのPDFチャンカーが従うインターフェース
    """
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def make_chunk(self, docs: list[Document]) -> list[Chunk]:
        pass

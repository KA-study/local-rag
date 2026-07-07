from abc import ABC, abstractmethod
from pathlib import Path

from program_files.shared.schemas import Document
from program_files.shared.schemas import Chunk
from program_files.shared.config import DEFAULT_PDF_PATH

#===========PDFLoader=================
class PDFLoaderBase(ABC):
    """
    すべてのPDFローダーが従うインターフェース
    """
    def __init__(self, file_path = DEFAULT_PDF_PATH):
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

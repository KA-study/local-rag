from pathlib import Path
from typing import List
from pypdf import PdfReader
import re

from pdf.base import PDFLoaderBase
from schemas import Document

class PypdfLoader(PDFLoaderBase):
    """
    pypdf実装のローダー
    """
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(self.file_path)

    def load_pdf(self) -> List[Document]:
        reader = PdfReader((str(self.file_path)))

        docs: List[Document] = []

        for page_number, page_text in enumerate(reader.pages):

            text = page_text.extract_text() or ""
            text = text.replace("\x00", "")

            text = _normalize_text(text)

            docs.append(
                Document(
                    page=page_number + 1,
                    text=text,
                    source=str(self.file_path)
                )
            )

        return docs


def _normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()

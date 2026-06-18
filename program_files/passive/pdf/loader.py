from pathlib import Path
from pypdf import PdfReader
import re

from program_files.passive.pdf._types import PDF_PATH
from program_files.passive.pdf.base import PDFLoaderBase
from program_files.app.registry.components_registry import ComponentsRegistry
from program_files.shared.schemas import Document


@ComponentsRegistry.component(
    base=PDFLoaderBase,
    name="py_pdf_loader"
)
class PypdfLoader(PDFLoaderBase):
    """
    pypdf実装のローダー
    """
    
    def __init__(self):
        self.file_path = Path(PDF_PATH)

        if not self.file_path.exists():
            raise FileNotFoundError(self.file_path)

    def load_pdf(self) -> list[Document]:
        reader = PdfReader((str(self.file_path)))

        docs: list[Document] = []

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

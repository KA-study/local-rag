from typing import List

from passive.pdf.loader import PypdfLoader
from passive.pdf._types import PDF_PATH
from passive.pdf.chunker import TokenChunker
from shared.schemas import Document, Chunk

def passive_operator():
    
    pdfloader = PypdfLoader(PDF_PATH)
    docs: List[Document] = pdfloader.load_pdf()

    pdfchunker = TokenChunker()
    chunks: List[Chunk] = pdfchunker.make_chunk(docs)

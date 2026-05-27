from typing import List

from passive.ingest.pdf.loader import PypdfLoader
from passive.ingest.pdf._types import PDF_PATH
from passive.ingest.pdf.chunker import TokenChunker
from shared.schemas import Document, Chunk

def passive_operator():
    
    pdfloader = PypdfLoader(PDF_PATH)
    docs: List[Document] = pdfloader.load_pdf()

    pdfchunker = TokenChunker()
    chunks: List[Chunk] = pdfchunker.make_chunk(docs)

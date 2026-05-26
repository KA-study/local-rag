from pdf.loader import PypdfLoader
from pdf.base import PDFLoaderBase
from pdf.chunker import TokenChunker

#==============PDFLoader====================
def create_pdf_loader(engine: str, file_path: str) -> PDFLoaderBase:

    if engine == "PypdfLoader":
        return PypdfLoader(file_path)

    raise ValueError(f"Unknown engine: {engine}")


#=============PDFChunker=====================
def create_pdf_chunker(engine: str) -> TokenChunker:

    if engine == "TokenChunker":
        return TokenChunker()

    raise ValueError(f"Unknown engine: {engine}")



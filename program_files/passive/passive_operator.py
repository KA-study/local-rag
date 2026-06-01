import numpy

from passive.pdf.loader import PypdfLoader
from passive.pdf.chunker import TokenChunker
from passive.service import  create_embedded_chunks
from infrastructure.embedding.embedder import STEmbedder
from infrastructure.vector_store.chroma_store import ChromaVectorStore
from shared.schemas import Document, Chunk, EmbeddedChunk

def passive_operator():
    
    #PDFload
    pdfloader = PypdfLoader()
    docs: list[Document] = pdfloader.load_pdf()

    #Chunknaize PDF
    pdfchunker = TokenChunker()
    chunks: list[Chunk] = pdfchunker.make_chunk(docs)

    #Embedding Chunk
    stembedder = STEmbedder()
    embedded_chunks: list[EmbeddedChunk] = create_embedded_chunks(chunks, stembedder)


    #Make VectorStore
    chroma_vector_store = ChromaVectorStore()
    chroma_vector_store.add(embedded_chunks)

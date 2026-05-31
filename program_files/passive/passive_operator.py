import numpy

from passive.pdf.loader import PypdfLoader
from passive.pdf.chunker import TokenChunker
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
    texts = [
        chunk.text for chunk in chunks
    ]

    chunk_embedder = STEmbedder()
    embeddings: numpy.ndarray = chunk_embedder.embed_batch(texts)

    embedded_chunks: list[EmbeddedChunk] = []

    for chunk, embedding in zip(
        chunks,
        embeddings
    ):
        embedded_chunks.append(
            EmbeddedChunk(
                chunk=chunk,
                embedding=embedding.tolist()
            )
        )


    #Make VectorStore
    chroma_vector_store = ChromaVectorStore()
    chroma_vector_store.add(embedded_chunks)

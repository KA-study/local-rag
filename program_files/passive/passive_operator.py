from program_files.passive.pdf.loader import PypdfLoader
from program_files.passive.pdf.chunker import TokenChunker
from program_files.passive.service import  create_embedded_chunks
from program_files.infrastructure.embedding.embedder import STEmbedder
from program_files.infrastructure.vector_store.chroma_store import ChromaVectorStore
from program_files.shared.schemas import Document, Chunk, EmbeddedChunk

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

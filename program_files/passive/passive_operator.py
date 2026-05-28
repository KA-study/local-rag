from passive.pdf.loader import PypdfLoader
from passive.pdf.chunker import TokenChunker
from passive.embedding.embedder import STEmbedder
from shared.schemas import Document, Chunk, EmbeddedChunk

def passive_operator():
    
    #PDFload
    pdfloader = PypdfLoader()
    docs: list[Document] = pdfloader.load_pdf()

    #Chunknaize PDF
    pdfchunker = TokenChunker()
    chunks: list[Chunk] = pdfchunker.make_chunk(docs)

    #Embedding Chunk
    chunk_embedder = STEmbedder()
    embeddings: list[EmbeddedChunk] = chunk_embedder.embed_batch(chunks)

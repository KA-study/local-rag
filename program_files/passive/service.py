import numpy

from infrastructure.embedding.base import BaseEmbedder
from shared.schemas import Chunk, EmbeddedChunk

def create_embedded_chunks(
    chunks: list[Chunk],
    chunk_embedder: BaseEmbedder,
) -> list[EmbeddedChunk]:

    texts = [
        chunk.text for chunk in chunks
    ]

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

    return embedded_chunks


